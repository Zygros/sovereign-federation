# OMEGA-10 Strict Ruff Gate Restoration and Post-Merge Phoenix Evidence — 2026-11-04

## Result

Private-to-public federation node `Zygros/omega-10` merged PR #5, restoring a blocking repository-wide Ruff check. The CI command is now `ruff check src tests` without the former `|| true` bypass. The 15 findings exposed by that gate were corrected across nine files, with regression coverage for invalid configuration types.

Merge commit: `5259035a273ca616ba4b2f9477e6d8ff815fbb1b`.

## Verification

- Pre-merge CI [41905659058](https://github.com/Zygros/omega-10/actions/runs/41905659058): Python 3.11 and 3.12 both passed strict Ruff, 11 pytest cases, and the local Phoenix benchmark.
- Pre-merge Phoenix Audit [41905659162](https://github.com/Zygros/omega-10/actions/runs/41905659162): success.
- Post-merge CI [41905813986](https://github.com/Zygros/omega-10/actions/runs/41905813986): both Python versions passed strict Ruff, 11 tests each, and the local Phoenix benchmark.
- Post-merge Phoenix Audit [41905813695](https://github.com/Zygros/omega-10/actions/runs/41905813695): success.

The local benchmark ran 420 components, injected corruption into 210, restored all 210, and reported recovery rate 1.0, preserved initial ledger prefix, valid six-event hash chain, and all component hashes verified.

## Independently verified post-merge artifacts

The two post-merge workflow ZIP artifacts were downloaded. Their ZIP digests independently matched the digests returned by GitHub:

- Python 3.11 artifact [13360865085](https://github.com/Zygros/omega-10/actions/runs/41905813986/artifacts/13360865085): `fb7b54f3ee98923fce85bbc52db973be0a8183c3f8b4f33cb394edf21bf6b04f`.
- Python 3.12 artifact [13360320907](https://github.com/Zygros/omega-10/actions/runs/41905813986/artifacts/13360320907): `e992ff7ce70656b2565a6078ab170e3004409040cd73e1bfbfbf332ffb5a23b7`.

For both artifacts, independent inspection found 420 baseline manifest entries, six ledger events, 210/210 recovery, and a valid independently recalculated ledger chain.

## Failure history

The initial strict CI run [41904139345](https://github.com/Zygros/omega-10/actions/runs/41904139345) failed as intended when the previously masked Ruff checks became blocking. It reported 15 findings. The code and tests were corrected; the final PR-head and post-merge runs passed. The bypass was not restored.

## Boundaries

This establishes repository-level lint/test execution and a deterministic local recovery fixture. It does not establish distributed recovery, external-agent participation, production deployment, or independent reproduction on a separate machine. The recovery result applies only to the 210 components in these runs.

## Source evidence

- [Merged OMEGA-10 PR #5](https://github.com/Zygros/omega-10/pull/5)
- [OMEGA-10 source report](https://github.com/Zygros/omega-10/blob/main/evidence/audits/2026-11-04-strict-ruff-gate-merge.md)
- [OMEGA-10 machine-readable receipt](https://github.com/Zygros/omega-10/blob/main/evidence/audits/2026-11-04-strict-ruff-gate-merge.json)
- [OMEGA-10 federation spine](https://github.com/Zygros/omega-10/blob/main/FEDERATION_SPINE.md)
