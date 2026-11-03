#!/usr/bin/env python3
"""Offline HOSSDA archive, PDF/OTS, and screenshot-byte reconciliation."""
import argparse, hashlib, json, pathlib, zipfile

CLAIMS = [{"filename":"STATUS REPORT — 195,943 CLICKS_261102_174726.pdf","sha256":"46091cc05043878b6861cb4785e04f78fb063103a8b01636b670bb70b9c1536d","block_height":974329,"screenshot":"Offical HOSSDA/Screenshot_20261102_204533_Chrome.jpg","screenshot_sha256":"7c64f815e31333ac6d80470c65684826f455bce488eee2ab7b0a27309ce90d97","pdf_expected":false},{"filename":"Geminis_proof_261102_174631.pdf","sha256":"680e1e12e6ceb45784e919398929e73ac913b9e962f96aa65c0ee291deeb6fd5","block_height":974329,"screenshot":"Offical HOSSDA/Screenshot_20261102_204455_Chrome.jpg","screenshot_sha256":"ff04eb154f87c2cabbc9e7eb476db7b3bbb5130822c75751ee5e136a2c939884","pdf_expected":false},{"filename":"The Golden Blueprint _261102_180629.pdf","sha256":"d8090963f4675eed69003667a4f7e74b59652b75a64ac188ad43133c571ec8ca","block_height":974333,"screenshot":"Offical HOSSDA/Screenshot_20261102_204632_Chrome.jpg","screenshot_sha256":"50fc5a3b8aa54f02ee2b531724ef141ecb05df441cbfc735963025b6da275bdc","pdf_expected":true},{"filename":"Geminis Reckoning _261102_181106.pdf","sha256":"8a8f59c6f4029186329274de72c7323544c886b3bc842a59cac62c4c7f18707f","block_height":974333,"screenshot":"Offical HOSSDA/Screenshot_20261102_204714_Chrome.jpg","screenshot_sha256":"d435b00f7f7c710430f05297352a72517ddd2ee871b8998ba4c577ee70699ed0","pdf_expected":true},{"filename":"Geminis Reflection_261102_181824.pdf","sha256":"88aa2b51b63c193e4fd3e5b5005039e5880a1193debb40dee995e847167a1fcc","block_height":974333,"screenshot":"Offical HOSSDA/Screenshot_20261102_204754_Chrome.jpg","screenshot_sha256":"8572c4dec21530f8b5bbc5c668800af5be977ce453573b75d5bef8bb0d5a33f4","pdf_expected":true},{"filename":"Geminis Remembrance_261102_182417.pdf","sha256":"f7e383989753a18fa82b6ea3f0eb5f225435c35c89169710093748909f41d6a9","block_height":974334,"screenshot":"Offical HOSSDA/Screenshot_20261102_204903_Chrome.jpg","screenshot_sha256":"b5bedc9f3615b4ae97cc7c2bbd76a77ebdc8e39cc03f2e54ec600f2fea439af1","pdf_expected":true},{"filename":"The Manifesto and SOE_261102_205657.pdf","sha256":"68c35e4ce3eb9e8bdaa65f904f6722d2cca42246059a94d31a03c87102790b19","block_height":974347,"screenshot":"Offical HOSSDA/HOSSDA_Master_Archive_261102/Screenshot_20261102_221118_Chrome.jpg","screenshot_sha256":"67ef5876307624ef8764433123a1634a9a1202ff157a29a9f76605791c65d17e","pdf_expected":true},{"filename":"Hyper-Omniscient SSDA_261102_211753.pdf","sha256":"3b884007c911df261a7f3cb54e06888e2964920fee4887b44fa49ea615248734","block_height":974351,"screenshot":"Offical HOSSDA/HOSSDA_Master_Archive_261102/Screenshot_20261102_221212_Chrome.jpg","screenshot_sha256":"61e1a934366f6999fec815643b64e3f7c0e73660782f2ca8916d019179e6a64f","pdf_expected":true},{"filename":"Significance Report HO-SSDA_261102_213022.pdf","sha256":"d2ddab6ac026a8406520a1ac976b7ee9cac18b6463e03eb3474bfd97ca755a94","block_height":974352,"screenshot":"Offical HOSSDA/HOSSDA_Master_Archive_261102/Screenshot_20261102_221539_Chrome.jpg","screenshot_sha256":"099a0372be600fbd08e30f87a933016817471a1de30a938be7d0ab6be90a710c","pdf_expected":true}]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def inspect(path):
    raw=path.read_bytes()
    out={"filename":path.name,"size_bytes":len(raw),"sha256":digest(raw),"zip_crc":"PASS","entries":[],"pdfs":[],"unpaired_ots":[]}
    with zipfile.ZipFile(path) as z:
        bad=z.testzip()
        if bad:
            out["zip_crc"]="FAIL"; out["zip_crc_failure_member"]=bad
        names=set(z.namelist())
        used=set()
        for name in sorted(n for n in names if not n.endswith("/")):
            data=z.read(name)
            kind="pdf" if name.lower().endswith(".pdf") else "ots" if name.lower().endswith(".ots") else "image" if name.lower().endswith((".jpg",".jpeg",".png",".webp")) else "other"
            out["entries"].append({"path":name,"size_bytes":len(data),"sha256":digest(data),"category":kind})
        for name in sorted(n for n in names if n.lower().endswith(".pdf")):
            h=hashlib.sha256(z.read(name)).digest()
            parent,_,base=name.rpartition("/")
            prefix=parent+"/" if parent else ""
            matches=[]
            for candidate in (prefix+base+".ots",prefix+base+" (1).ots"):
                if candidate in names and h in z.read(candidate):
                    matches.append(candidate); used.add(candidate)
            out["pdfs"].append({"path":name,"sha256":h.hex(),"ots_digest_match":bool(matches),"matching_receipts":matches})
        out["unpaired_ots"]=sorted(n for n in names if n.lower().endswith(".ots") and n not in used)
    counts={}
    for entry in out["entries"]:
        counts[entry["category"]]=counts.get(entry["category"],0)+1
    out["counts"]=counts
    return out

def build(paths):
    archives=[inspect(pathlib.Path(p)) for p in paths]
    members={}
    for path in map(pathlib.Path,paths):
        with zipfile.ZipFile(path) as z:
            for name in z.namelist():
                if not name.endswith("/"): members[name]=z.read(name)
    archive_receipts=[]
    for target in map(pathlib.Path,paths):
        h=hashlib.sha256(target.read_bytes()).digest()
        for name,data in members.items():
            if name.rsplit("/",1)[-1]==target.name+".ots":
                archive_receipts.append({"target":target.name,"sha256":h.hex(),"receipt":name,"digest_match":h in data})
    screenshots=[]
    for claim in CLAIMS:
        screen=members.get(claim["screenshot"])
        h=bytes.fromhex(claim["sha256"])
        pdfs=[n for n,b in members.items() if n.lower().endswith(".pdf") and hashlib.sha256(b).digest()==h]
        ots=[n for n,b in members.items() if n.lower().endswith(".ots") and h in b]
        screenshots.append({**claim,"screenshot_present":screen is not None,
          "screenshot_hash_match":screen is not None and digest(screen)==claim["screenshot_sha256"],
          "pdf_present_and_hash_match":bool(pdfs),"pdf_paths":pdfs,
          "ots_receipt_contains_digest":bool(ots),"ots_paths":ots,
          "evidence_class":"user-supplied OpenTimestamps browser SUCCESS screenshot; image bytes and digest correspondence checked; proof not replayed here"})
    unique_pdfs={x["sha256"] for a in archives for x in a["pdfs"]}
    return {"schema":"conzetian.hossda.archive-evidence.v1","author":"Justin Neal Thomas Conzet",
      "observation_date":"2026-11-03","method":"ZIP CRC, SHA-256, PDF-to-OTS digest presence, screenshot-byte hash and manually transcribed browser attestation reconciliation",
      "archives":archives,"archive_receipt_checks":archive_receipts,"screenshot_attestations":screenshots,
      "screenshot_summary":{"total":len(screenshots),"screenshot_hash_matches":sum(x["screenshot_hash_match"] for x in screenshots),
        "pdf_targets_present":sum(x["pdf_present_and_hash_match"] for x in screenshots),
        "pdf_targets_missing":sum(not x["pdf_present_and_hash_match"] for x in screenshots),
        "block_heights":sorted({x["block_height"] for x in screenshots})},
      "unique_pdf_sha256_count":len(unique_pdfs),
      "limits":["No independent OTS proof replay or Bitcoin Merkle-path validation","Block-height existence is independently checked via public explorers; this does not authenticate screenshots",
        "No device, Tor, x402, Arweave/AO, wallet, or Google API runtime access","No authorship/copyright determination"]}

def main():
    p=argparse.ArgumentParser(); p.add_argument("archives",nargs="+",type=pathlib.Path); p.add_argument("--json",type=pathlib.Path); a=p.parse_args()
    report=build(a.archives); encoded=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if a.json: a.json.parent.mkdir(parents=True,exist_ok=True); a.json.write_text(encoded,encoding="utf-8")
    print(encoded,end="")
    good=all(x["zip_crc"]=="PASS" and all(y["ots_digest_match"] for y in x["pdfs"]) for x in report["archives"])
    good=good and all(x["digest_match"] for x in report["archive_receipt_checks"])
    good=good and all(x["screenshot_hash_match"] and x["ots_receipt_contains_digest"] for x in report["screenshot_attestations"])
    return 0 if good else 1

if __name__=="__main__": raise SystemExit(main())
