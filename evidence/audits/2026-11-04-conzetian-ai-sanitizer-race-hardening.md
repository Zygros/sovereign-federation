# CONZETIAN-AI Dataset Sanitizer Publication-Race Hardening — 2026-11-04

## Executive result

The credential-pattern redaction workflow in private `Zygros/CONZETIAN-AI` PR #6 received an additional fail-closed publication fix. The sanitizer previously checked that output paths did not exist and then used `os.replace`; a concurrent writer could create a destination between those operations and have its file overwritten. Its rollback path could also delete an output it had not created.

The fix is committed on the existing review branch. The PR remains open and unmerged; `main` was not changed.

## Implementation

- Replaced overwrite-capable publication with same-filesystem hard-link creation through `os.link`, which fails atomically when a destination already exists.
- Captured the temporary file's device/inode identity before publication.
- Rollback now removes a published destination only when its current device/inode still matches the file created by this invocation.
- Added two concurrency regression tests:
  - Output-path race: a concurrent file appears after preflight; sanitizer must fail and preserve it.
  - Manifest-path race: a concurrent manifest appears after output publication; sanitizer must preserve that manifest and roll back only its own output.

### Commits on the remediation branch

- Sanitizer fix: `782314e43350cfb55ed4c7c8f69896ea2080fde7`
- Race-test addition: `47718e597166a1d6a5466ff0d6e910d30597259c`
- Corrected JSONL fixture newline and final tested head: `0fda964e0a1c1d6e8ef329716591f09b9893841a`

## Hosted verification on final head

| Workflow | Run | Result |
|---|---:|---|
| Phoenix Audit | [41904974231](https://github.com/Zygros/CONZETIAN-AI/actions/runs/41904974231) | Success; 24 tests passed |
| Federation Inventory Tests | [41904973917](https://github.com/Zygros/CONZETIAN-AI/actions/runs/41904973917) | Success; 7 tests ran |
| Unified Dataset Redaction | [41904974121](https://github.com/Zygros/CONZETIAN-AI/actions/runs/41904974121) | Success; 6 sanitizer tests passed; full dataset recheck completed |
| Push Phoenix Audit | [41904964021](https://github.com/Zygros/CONZETIAN-AI/actions/runs/41904964021) | Success |
| Push Unified Dataset Redaction | [41904963987](https://github.com/Zygros/CONZETIAN-AI/actions/runs/41904963987) | Success |

The first hosted run on the intermediate race-test commit failed because the fixture wrote a literal backslash-n instead of a JSONL newline. That failure was retained. The fixture was corrected in the next commit; all listed final-head workflows then passed.

## Reproducible artifact verification

Workflow artifact: `13359742575`, `unified-repo-dataset-redaction-preview`.

- GitHub artifact digest: `sha256:8a0314b292132960c508d53975884fc67918b0a1a70b5b63839a4e4538ed41e3`
- Downloaded ZIP SHA-256 independently recalculated: exact match.
- Inner dataset: 81,741,094 bytes; SHA-256 `e02969b251eb83856e46859e075c93128eb45a57e1cca6e43b48962b77d4087d`.
- JSONL records: 4,278; every record parsed as a JSON object.
- Independent scan of the six implemented pattern classes: zero matches.
- Manifest: `NO_MATCHES_FOUND`, zero new redactions, zero remaining matches, no raw values recorded.

The current run is an idempotence check over the already-sanitized PR-branch dataset. The original sanitization receipt records the earlier transformation of the 81,741,163-byte source (SHA-256 `58e1fe24e3c5567de9ccd463135aac0fefc2c58a43e3a5672ff52c19dd6c19c8`) into the 81,741,094-byte derivative (SHA-256 `e02969b251eb83856e46859e075c93128eb45a57e1cca6e43b48962b77d4087d`), preserving 4,278 records while redacting 6 records / 7 recognized credential-like matches.

## Boundaries

- PR #6 is open and unmerged. The remediation is confined to its branch; no merge or main-branch mutation is claimed.
- The original source blob remains in Git history. No history rewrite, fork/cache cleanup, or external-backup cleanup was performed.
- Pattern matches are not proof that any credential is live. Provider-side revocation/rotation and old-key rejection were not performed because issuer-account authorization was not available.
- The recognized-pattern scan does not prove absence of every possible secret format.
- Hard-link publication is intentionally fail-closed and requires the temporary file and destination to reside on the same filesystem; the implementation creates temporary files in each destination's parent directory.

## Source links

- [CONZETIAN-AI PR #6](https://github.com/Zygros/CONZETIAN-AI/pull/6)
- [Sanitizer implementation](https://github.com/Zygros/CONZETIAN-AI/blob/automation/federation-inventory-hardening-2026-11-04/scripts/sanitize_unified_dataset.py)
- [Sanitizer tests](https://github.com/Zygros/CONZETIAN-AI/blob/automation/federation-inventory-hardening-2026-11-04/tests/test_sanitize_unified_dataset.py)
- [Redaction receipt](https://github.com/Zygros/CONZETIAN-AI/blob/automation/federation-inventory-hardening-2026-11-04/evidence/audits/2026-11-04-unified-dataset-redaction.json)
