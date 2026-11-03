#!/usr/bin/env python3
"""Offline ZIP/PDF/OTS digest inventory. Does not verify Bitcoin attestations."""
import argparse
import hashlib
import json
import pathlib
import zipfile


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def inspect_archive(path):
    raw = path.read_bytes()
    result = {
        "filename": path.name,
        "size_bytes": len(raw),
        "sha256": sha256(raw),
        "zip_crc": "PASS",
        "entries": [],
        "pdfs": [],
        "unpaired_ots": [],
    }
    with zipfile.ZipFile(path) as zf:
        bad = zf.testzip()
        if bad is not None:
            result["zip_crc"] = "FAIL"
            result["zip_crc_failure_member"] = bad
        names = set(zf.namelist())
        for name in sorted(n for n in names if not n.endswith("/")):
            data = zf.read(name)
            category = ("pdf" if name.lower().endswith(".pdf") else
                        "ots" if name.lower().endswith(".ots") else
                        "image" if name.lower().endswith((".jpg", ".jpeg", ".png", ".webp")) else "other")
            result["entries"].append({
                "path": name, "size_bytes": len(data),
                "sha256": sha256(data), "category": category,
            })
        used = set()
        for name in sorted(n for n in names if n.lower().endswith(".pdf")):
            digest = hashlib.sha256(zf.read(name)).digest()
            parent, _, basename = name.rpartition("/")
            prefix = parent + "/" if parent else ""
            candidates = [prefix + basename + ".ots", prefix + basename + " (1).ots"]
            matches = []
            for candidate in candidates:
                if candidate in names and digest in zf.read(candidate):
                    matches.append(candidate)
                    used.add(candidate)
            result["pdfs"].append({
                "path": name, "sha256": digest.hex(),
                "ots_digest_match": bool(matches), "matching_receipts": matches,
            })
        result["unpaired_ots"] = sorted(
            n for n in names if n.lower().endswith(".ots") and n not in used
        )
    counts = {}
    for entry in result["entries"]:
        counts[entry["category"]] = counts.get(entry["category"], 0) + 1
    result["counts"] = counts
    return result


def build_report(paths):
    archives = [inspect_archive(pathlib.Path(p)) for p in paths]
    archive_receipts = []
    for target in map(pathlib.Path, paths):
        target_digest = hashlib.sha256(target.read_bytes()).digest()
        for source in archives:
            for entry in source["entries"]:
                if entry["category"] == "ots" and pathlib.PurePosixPath(entry["path"]).name == target.name + ".ots":
                    with zipfile.ZipFile(pathlib.Path(paths[archives.index(source)])) as zf:
                        proof = zf.read(entry["path"])
                    archive_receipts.append({
                        "target": target.name, "target_sha256": target_digest.hex(),
                        "receipt_archive": source["filename"], "receipt": entry["path"],
                        "digest_match": target_digest in proof,
                        "scope": "digest-presence-only; not full OTS/Bitcoin verification",
                    })
    unique_pdfs = {p["sha256"] for a in archives for p in a["pdfs"]}
    return {
        "schema": "conzetian.hossda.archive-evidence.v1",
        "author": "Justin Neal Thomas Conzet",
        "observation_date": "2026-11-03",
        "method": "ZIP CRC, SHA-256 inventory, and digest-byte presence in sibling OTS receipts",
        "archives": archives,
        "archive_receipt_checks": archive_receipts,
        "unique_pdf_sha256_count": len(unique_pdfs),
        "verification_boundary": [
            "No full OpenTimestamps proof-tree verification",
            "No Bitcoin block-header or Merkle-path verification",
            "No authorship or copyright ownership determination",
            "No device, Tor, x402, Arweave/AO, or Google API runtime probe",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archives", nargs="+", type=pathlib.Path)
    parser.add_argument("--json", type=pathlib.Path)
    args = parser.parse_args()
    report = build_report(args.archives)
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    good = all(a["zip_crc"] == "PASS" and all(p["ots_digest_match"] for p in a["pdfs"]) for a in report["archives"])
    good = good and all(x["digest_match"] for x in report["archive_receipt_checks"])
    return 0 if good else 1


if __name__ == "__main__":
    raise SystemExit(main())
