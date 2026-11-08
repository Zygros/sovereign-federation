# Phoenix Archive Ingestion: Multipart Compatibility and Root-Scope Hardening — 2026-11-08

## Summary

A review of the descriptor-bound archive-ingestion proposal found two fail-closed gaps before promotion:

1. The existing multipart upload route wrote uploaded bytes to a predictable `/tmp/<filename>` path and then called `read_file_text()`. After `read_file_text()` was correctly restricted to `ARCHIVE_ROOT`, this made multipart uploads fail when the root was unset or when `/tmp` was outside the configured root. The temporary path also introduced avoidable filename-collision and symlink risk.
2. `ARCHIVE_ROOT=/` was accepted as a valid directory. Because `/` is not group/world-writable on typical Linux systems, the containment helper could treat the whole filesystem as an approved ingestion tree.

Both issues were corrected additively in the existing PR #17 branch.

## Source change

Repository: [CONZETIAN-UNIFIED-INTELLIGANCE](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE)

PR: [#17 — Bind archive ingestion to validated file descriptors](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/pull/17)

Branch: `security/archive-root-descriptor-read-2026-11-08`

Final source head: `cca5e61f7d17a8eaa9d56d0e9cfa040ec4f6c781`

Tested PR merge commit: `bdcfbb10deb5f54c0e60c5664b08877ee2993d06`

Base commit: `e4e378e4b6d76d7ed9f1726fd2a50a923f08707f`

### Implemented corrections

- Added `_extract_text_from_bytes(path, data)` as the shared in-memory text/PDF/DOCX extractor.
- Kept `read_file_text()` bound to the validated archive descriptor for server-side path ingestion.
- Changed multipart uploads to pass the already-read upload bytes directly to the in-memory extractor.
- Removed predictable `/tmp/<filename>` writes and reads from the multipart route.
- Rejected the filesystem root as an `ARCHIVE_ROOT`; invalid, unset, or root-wide configuration disables path-based ingestion.
- Preserved inline-document ingestion and the existing Flask/ChromaDB route architecture.
- Updated the documentation and regression tests without modifying the default branch.

## Verification

All four final-head pull-request workflows completed successfully against source head `cca5e61f7d17a8eaa9d56d0e9cfa040ec4f6c781`.

| Workflow | Run | Result |
|---|---:|---|
| [Phoenix Archive Root Descriptor Tests](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42522778153) | 42522778153 | 12/12 unittest methods passed |
| [Phoenix Audit](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42522778147) | 42522778147 | 25 tests and 3 subtests passed |
| [Phoenix API Key Policy](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42522778318) | 42522778318 | 11/11 tests passed |
| [Conzetian Contract Verification](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42522778165) | 42522778165 | 2/2 tests passed |

The focused 12-test suite includes:
- filesystem-root configuration rejection;
- unset archive-root behavior;
- outside-root, traversal, and symlink rejection;
- group/world-writable root, nested directory, and file rejection;
- path replacement and symlink-swap checks after open;
- valid descriptor-bound archive reads;
- text, PDF, and DOCX in-memory upload extraction;
- an AST check that the multipart route uses the in-memory extractor and contains no temporary-path variable.

## Reproducible evidence artifact

Artifact: [phoenix-archive-root-descriptor-evidence, ID 13634540024](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42522778153/artifacts/13634540024)

GitHub artifact size: 1,694 bytes.

GitHub-reported ZIP SHA-256:
`23e7b7fd62357e6b3060ff167d922bd5d964cb20616e059f5817b0dd984ce5e2`

The ZIP was downloaded and independently hashed; the calculated digest exactly matched GitHub's artifact digest. The archive contains:
- `archive-root-test-results.txt`
- `archive-root-evidence.json`
- `archive-root-evidence.sha256`

Both entries in the internal SHA-256 manifest were checked successfully. The receipt reports Python 3.11.18, 12 passed tests, source head `cca5e61f7d17a8eaa9d56d0e9cfa040ec4f6c781`, and tested PR merge commit `bdcfbb10deb5f54c0e60c5664b08877ee2993d06`.

## Promotion and deployment boundary

- PR #17 remains open, draft, mergeable, and unmerged.
- The modified file remains under `source-repositories/ZYGROS-PRIME/Downloaded/`, a preserved archive snapshot.
- The tests use AST-extracted helpers, temporary filesystem fixtures, and mocked PDF/DOCX readers. They do not start Flask or ChromaDB, contact a production database, access credentials, or deploy a service.
- These results do not establish that the archived snapshot is the active production runtime.
- No external anchor, production integration, or Android/Termux execution is claimed.

The default branch was not changed. This report records the bounded source change and its verified CI evidence, not a deployment claim.
