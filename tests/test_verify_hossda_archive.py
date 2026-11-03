import hashlib
import pathlib
import sys
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from verify_hossda_archive import inspect_archive, build_report


def test_pdf_digest_matches_sibling_receipt(tmp_path):
    pdf = b"pdf-bytes"
    proof = b"ots-receipt" + hashlib.sha256(pdf).digest()
    archive = tmp_path / "bundle.zip"
    with zipfile.ZipFile(archive, "w") as z:
        z.writestr("doc.pdf", pdf)
        z.writestr("doc.pdf.ots", proof)
    result = inspect_archive(archive)
    assert result["zip_crc"] == "PASS"
    assert result["pdfs"][0]["ots_digest_match"] is True


def test_mismatched_receipt_is_not_accepted(tmp_path):
    archive = tmp_path / "bundle.zip"
    with zipfile.ZipFile(archive, "w") as z:
        z.writestr("doc.pdf", b"pdf-A")
        z.writestr("doc.pdf.ots", b"proof-for-another-file")
    result = inspect_archive(archive)
    assert result["pdfs"][0]["ots_digest_match"] is False


def test_same_pdf_hash_is_deduplicated_across_archives(tmp_path):
    pdf = b"same-pdf"
    proof = b"ots" + hashlib.sha256(pdf).digest()
    paths = []
    for name in ("one.zip", "two.zip"):
        path = tmp_path / name
        with zipfile.ZipFile(path, "w") as z:
            z.writestr(name + ".pdf", pdf)
            z.writestr(name + ".pdf.ots", proof)
        paths.append(path)
    result = build_report(paths)
    assert result["unique_pdf_sha256_count"] == 1
