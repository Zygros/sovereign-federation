# Phoenix API and Audit Integrity Review — 2026-11-01

## Scope

Sanitized review of the private Phoenix API security branch, the private-node receipt-contract workflow, and the federation's Python audit pipeline. This public record contains no credential values, wallet contents, or private source payloads.

## Federation inventory

The authenticated GitHub listing returned **26 repositories**: **21 public** and **5 private**. The current `FEDERATION_INDEX.json` contains 26 nodes and matches the live repository names and visibility classifications exactly.

- Index blob: `a23401d76dd85810a966a320ff31cda0591a055f`
- Historical index timestamp: `2026-10-23T19:27:33Z`
- Missing names: 0
- Extra names: 0
- Visibility mismatches: 0

The index was not rewritten merely to refresh its timestamp.

## Phoenix API authentication hardening

Private source review: [CONZETIAN-UNIFIED-INTELLIGANCE PR #7](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/pull/7), still open and unmerged.

The review branch now rejects API keys containing fewer than **32 non-whitespace characters** at startup, in addition to rejecting missing/blank and known weak keys. Validation occurs before ChromaDB initialization. The configured key is not included in the rejection log. The shell integration script and security documentation were updated, and a standard-library regression suite covers missing/blank, known weak, 31-character, whitespace-padded, exactly-32-character, and 64-character cases.

- API-key policy workflow: [run 41346979725](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/41346979725) completed successfully with **6 tests run** on commit `8677144a382f06851e7245b14cbfe9bd96e7b58e`.
- Later documentation/workflow head: `f8d2808e8946c9dbeb34af5d981a98adf31ca2fb`. No fresh API-policy run was returned for that later head; the code and test files were unchanged after the successful six-test run.
- [Phoenix Audit run 41346979691](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/41346979691) reported success but logged `find: ... Broken pipe` and `find: write error`; the Python compile/test branch was skipped. This green result is not treated as Python verification.
- [Contract Verification run 41346979781](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/41346979781) failed because the base workflow selected Python 3.15.1 without installing pytest.

The separate workflow repair [PR #11](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/pull/11) pins Python 3.11, installs `pytest==9.2.0`, and limits workflow permissions to `contents: read`. Its [Contract Verification run 41233324790](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/41233324790) passed **2 tests**; [Phoenix Audit run 41233324853](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/41233324853) also passed. PR #11 remains open and unmerged, so the base-branch contract workflow failure remains until that repair reaches main.

## Phoenix Audit false-negative repair

The first honest source-probe repair was developed in the superseded [PR #12](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/pull/12), then carried forward into [PR #14](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/pull/14), which is open and unmerged.

The repair replaces the `find | grep -q` pipeline under `pipefail` with `find -print -quit` captured through command substitution. It adds regression checks for active-source, empty-tree, and archive-only cases. It also repairs malformed usage strings in three active `Downloaded/` helper files and scopes pytest to the repository-root `tests/` or `test/` directory rather than recursively collecting tests from imported projects with separate dependency environments.

### Discovery and repair chronology

- [Probe regression run 41347435296](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/41347435296) passed the initial positive/negative source-discovery tests.
- [First honest Phoenix Audit run 41347435298](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/41347435298) exposed 12 syntax errors: 3 in active `Downloaded/` helpers and 9 in the preserved `source-repositories/ZYGROS-PRIME/Unpacked/` export archive.
- The 3 active usage-string defects were repaired. The 9 archived files were left untouched; only the exact `Unpacked/` subtree is excluded from active-source discovery and compileall. The archive is not claimed as syntactically valid.
- The first unscoped pytest attempt exposed 11 collection errors from imported projects requiring dependencies such as FastAPI, LiveKit, and project-specific packages. The generic workflow now runs only repository-root tests.
- [Final Phoenix Audit run 41347955169](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/41347955169) completed successfully. Its Python step completed, repository-root pytest reported **2 passed in 0.01s**, and Node, Go, Rust, Java, and Secret patterns steps all completed successfully.
- [Final Phoenix Audit Probe Regression run 41347954991](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/41347954991) completed successfully, including the archive-only and root-test-scope assertions.
- [Contract Verification run 41347955005](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/41347955005) remains failed on the base workflow because Python 3.15.1 had no pytest. The separate PR #11 repair remains open and unmerged.

PR #12 and PR #13 were closed as superseded; their branches and commits were preserved. PR #14 is the current review branch.

## Verification boundaries

- The six API-key policy tests passed on the earlier source head; no fresh run is claimed for the later documentation/workflow head.
- The Phoenix Audit result verifies the active source tree and root tests under the revised scope. The preserved `Unpacked/` archive remains excluded and unvalidated.
- Imported projects' tests are not run by this generic root workflow; they retain their own dependency and test environments.
- No production deployment, credential rotation, Git history rewrite, Google Drive scan, OTS verification, Bitcoin confirmation, Arweave/AO read-back, or external anchor is claimed.
