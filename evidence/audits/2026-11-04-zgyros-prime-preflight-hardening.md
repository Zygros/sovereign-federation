# ZYGROS-PRIME Phoenix Preflight Formatting and CI Hardening — 2026-11-04

## Additive changes

On the existing draft [ZYGROS-PRIME PR #6](https://github.com/Zygros/ZYGROS-PRIME/pull/6), the bounded HTC and federation simulators and the HTC test file were normalized to the repository's Black formatter. The existing Python CI workflow now runs on the preflight branch as well as the default development branches, and includes a read-only Black diff step before the enforcement check.

Files changed:
- `scripts/omega_htc_sim.py`
- `scripts/omega_federation_sim.py`
- `tests/test_omega_htc_sim.py`
- `.github/workflows/python-ci.yml`

No simulation behavior or architecture was intentionally changed. The simulator documentation continues to distinguish synthetic optimization and coverage from live agents, real distributed nodes, or physical time acceleration.

## Final-head verification

Final branch head: `50cb96e75dc67ccfa808622468e7a71d5e3e0d62`.

| Check | Workflow run | Result |
|---|---:|---|
| OmniNet Python CI | [41911501205](https://github.com/Zygros/ZYGROS-PRIME/actions/runs/41911501205) | SUCCESS on Python 3.10, 3.11, and 3.12 |
| Omega HTC Simulation Tests | [41911501635](https://github.com/Zygros/ZYGROS-PRIME/actions/runs/41911501635) | SUCCESS |
| Phoenix Audit, including credential-pattern scan | [41911501255](https://github.com/Zygros/ZYGROS-PRIME/actions/runs/41911501255) | SUCCESS |
| HTC Claim Audit | [41911501014](https://github.com/Zygros/ZYGROS-PRIME/actions/runs/41911501014) | Deterministic audit and artifact upload succeeded; external provenance attestation blocked |

Each Python matrix job passed 15 tests, for 45 test executions across Python 3.10/3.11/3.12. Compilation and the configured flake8 checks passed in each job. Black reported all four checked files unchanged, and the enforced `black --check` passed in each matrix job.

## Claim-audit artifact

The deterministic claim-audit workflow uploaded [artifact 13360914932](https://github.com/Zygros/ZYGROS-PRIME/actions/runs/41911501014/artifacts/13360914932). It was independently downloaded and inspected.

- ZIP size: 666 bytes.
- ZIP SHA-256: `57f81471bad897eed2f89c584d221b935b6308602bc35629dc51afa6d49981ee`, matching GitHub's artifact digest.
- Contains `latest_claim_audit.json`, 1,158 bytes; SHA-256 `bccc487a9a08ab20764183462c9e4573e905bfb0dfc5458b3abfa688658f076a`.
- The receipt records 10 claims: 4 verified, 0 refuted, and 6 unresolved.
- Verified entries are limited to the recorded phi definition, the (2^{26}) arithmetic, registry presence, and execution-report presence. Other listed claims remain unverified or theoretical.

## Exact attestation blocker

The deterministic audit and artifact upload completed successfully. The final workflow step failed because GitHub returned:

`Feature not available for user-owned private repositories. To enable this feature, please make this repository public.`

The repository remains private. No visibility change was made. The artifact exists, but it does **not** have the requested GitHub artifact provenance attestation. This is a GitHub product/visibility prerequisite, not a failure of the deterministic claim-audit step.

## Status and limits

- PR #6 remains draft, open, and unmerged; GitHub reported `mergeable=false` at the final read-back.
- No deployment, live distributed integration, production operation, or external provenance attestation is claimed.
- The deterministic audit's 4 verified / 6 unresolved split is preserved as-is; no unresolved claim was promoted.
- The branch-specific CI trigger and Black diagnostic are additive. No default-branch merge was performed.

Machine-readable receipt: [2026-11-04-zgyros-prime-preflight-hardening.json](2026-11-04-zgyros-prime-preflight-hardening.json).
