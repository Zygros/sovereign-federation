import hashlib
import pathlib
import sys
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from verify_hossda_archive import inspect, build


def test_pdf_receipt_digest_match(tmp_path):
    data = b"pdf bytes"
    proof = b"ots" + hashlib.sha256(data).digest()
    path = tmp_path / "x.zip"
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("x.pdf", data)
        z.writestr("x.pdf.ots", proof)
    assert inspect(path)["pdfs"][0]["ots_digest_match"]


def test_mismatched_receipt_is_rejected(tmp_path):
    path = tmp_path / "x.zip"
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("x.pdf", b"pdf")
        z.writestr("x.pdf.ots", b"other")
    assert not inspect(path)["pdfs"][0]["ots_digest_match"]


def test_zip_crc_and_pdf_count(tmp_path):
    path = tmp_path / "x.zip"
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("a.pdf", b"a")
    result = inspect(path)
    assert result["zip_crc"] == "PASS"
    assert result["counts"]["pdf"] == 1


def test_screenshot_evidence_claims_are_recorded():
    from verify_hossda_archive import CLAIMS
    assert len(CLAIMS) == 9
    assert {c["block_height"] for c in CLAIMS} == {974329, 974333, 974334, 974347, 974351, 974352}
