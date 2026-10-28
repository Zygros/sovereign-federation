# Omega-10 strict-lint recovery — 2026-10-28

**Observed at (UTC):** 2026-10-28T19:21:56Z  
**Evidence class:** `TESTED`  
**Scope:** One targeted lint repair on the open Omega-10 Phoenix recovery/benchmark PR branch. This is not a full source audit or production deployment.

## Failure reproduced from GitHub Actions

- Repository: [Zygros/omega-10](https://github.com/Zygros/omega-10)
- Open code review: [PR #1](https://github.com/Zygros/omega-10/pull/1)
- Failing CI run: [39838393636](https://github.com/Zygros/omega-10/actions/runs/39838393636), commit `0408380366a1970a640234a9d802419cae773646`
- Both Python 3.11 and 3.12 jobs stopped at the strict `ruff check .` gate; pytest was skipped.
- The decoded logs identify two findings in `scripts/mmap_ring_benchmark.py`: `EXE001` (a shebang on a non-executable file) and `UP017` (use `datetime.UTC` instead of `timezone.utc`).

## Additive repair

- Fix commit: [`f08668c4b5b06f55b116a262f88c6d429c158d6e`](https://github.com/Zygros/omega-10/commit/f08668c4b5b06f55b116a262f88c6d429c158d6e)
- Changed path: `scripts/mmap_ring_benchmark.py` only.
- Replaced `from datetime import datetime, timezone` with `from datetime import UTC, datetime`, and `datetime.now(timezone.utc)` with `datetime.now(UTC)`.
- Set the tracked file mode to `100755` so its existing Python shebang matches the executable bit.
- Prior blob SHA: `7ed8865b9c33f2ec9ee9cc286bca9e11035954f2`.
- New blob SHA: `19c362025637571b9c38309984757b854cd1d564`.
- Parent commit: `0408380366a1970a640234a9d802419cae773646`.

## Verification after repair

All cited runs target the fix commit `f08668c4b5b06f55b116a262f88c6d429c158d6e`.

- [CI run 40753589925](https://github.com/Zygros/omega-10/actions/runs/40753589925): **SUCCESS**. Python 3.11 and 3.12 both passed strict repository-wide Ruff and the full pytest suite.
- [Phoenix Audit push run 40753579774](https://github.com/Zygros/omega-10/actions/runs/40753579774): **SUCCESS**.
- [Phoenix Audit pull-request run 40753589935](https://github.com/Zygros/omega-10/actions/runs/40753589935): **SUCCESS**.
- The open PR remains open and unmerged; this evidence does not imply a merge.

## Boundaries

The benchmark remains a local, reproducible microbenchmark. These workflow results do not establish production deployment, durable-storage IOPS, external timestamp anchoring, OpenTimestamps verification, credential remediation, or a full audit of Omega-10. Existing history and evidence were preserved; no prior claim was promoted beyond the checks that actually passed.
