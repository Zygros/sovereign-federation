# Phoenix execution checkpoint — 2026-11-06

## Scope

This checkpoint records the current connected GitHub inventory, the final-head CI dependency reconciliation for ZYGROS-PRIME PR #10, the completed Phoenix/Ghost launcher verification for PR #9, and the security boundary on the CONZETIAN-AI dataset-redaction PR.

## Repository inventory

The authenticated GitHub connector returned 26 repositories owned by Zygros: 21 public and 5 private. The inventory is a visibility/availability snapshot, not a claim that every repository is healthy, deployed, or externally reachable.

## ZYGROS-PRIME PR #10 — strict canonical Python CI

PR: https://github.com/Zygros/ZYGROS-PRIME/pull/10

The first strict-CI branch revision installed CI tools but did not install the repository's declared `requirements.txt`, despite including `requirements.txt` in the workflow path filters and the previous workflow having installed project dependencies. The workflow label also implied project dependencies were installed.

A follow-up commit restored the declared dependency installation as a separate, explicit step before strict CI tooling:

- Branch: `ci/strict-canonical-python-2026-11-05`
- Final head: `8fe5c4ea3f12a8095bbf382eb5662895a48d30d3`
- Changed file: `.github/workflows/python-ci.yml`
- Commit: `8fe5c4ea3f12a8095bbf382eb5662895a48d30d3`
- PR remains open, non-draft, mergeable, and unmerged.

Final-head workflow:

- OmniNet Python CI run: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42285809483
- Conclusion: `success`
- Matrix: Python 3.8, 3.9, 3.10, 3.11; all four jobs completed successfully.
- Every matrix job completed declared `requirements.txt` installation, strict CI tool installation, compileall/py_compile, critical flake8, Black on `tests/`, mypy, and canonical pytest.
- Each matrix job reported `3 passed`.
- Each matrix job reported `Success: no issues found in 11 source files` from mypy.
- The Python 3.8 job log confirms the declared dependency install executed from `requirements.txt`, including requests, numpy, aiohttp, asyncio, pandas, cryptography, pycryptodome, python-dotenv, PyYAML, pytest, pytest-asyncio, Black, flake8, mypy, and Sphinx.

The three non-Python-CI workflows below passed on the immediately preceding source head `b3a90f19709252508d445928ca25f44999aeac91`. The follow-up commit changed only the Python CI dependency-install steps; these workflow results are predecessor-head evidence, not reruns on the final head:

- Phoenix Audit: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42106866317
- Repository Quality Gate: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42106866292
- HTC Claim Audit: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42106866590

The HTC claim receipt classified 10 claims as 4 verified, 0 refuted, and 6 unresolved. Artifact 13451972559 was recorded with SHA-256 `f0c97b496e8ff1625425fc88419a98c1a0e0a082629f6f8ab6f073d84847a576`.

## ZYGROS-PRIME PR #9 — Phoenix/Ghost launcher preflight

PR: https://github.com/Zygros/ZYGROS-PRIME/pull/9

- Final head: `b2d3c77b0f879ae1857bd10b17e58b3187a93aa3`
- Phoenix Launcher Safety Tests: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42107167223 — success.
- Phoenix Audit: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42107167254 — success.
- Repository Quality Gate: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42107167454 — success.
- HTC Claim Audit: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42107167407 — success.
- OmniNet Python CI: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42107167408 — all four Python 3.8–3.11 jobs completed successfully.

The launcher job log contains six token-store PASS assertions and fourteen launcher preflight PASS assertions. The local dual-runtime case used a stubbed tmux executable; no real session or deployment was started. The current default branch still lacks the Phoenix/Ghost runtime files, so the launchers correctly fail closed when those files are absent.

The PR description was corrected to record the completed Python 3.11 result rather than the earlier in-progress observation. PR #9 remains open, non-draft, mergeable, and unmerged.

## CONZETIAN-AI PR #6 — dataset redaction security boundary

PR: https://github.com/Zygros/CONZETIAN-AI/pull/6

Current branch-head workflows were read back as successful:

- Federation Inventory Tests: https://github.com/Zygros/CONZETIAN-AI/actions/runs/41909782929
- Phoenix Audit: https://github.com/Zygros/CONZETIAN-AI/actions/runs/41909782796
- Unified Dataset Redaction: https://github.com/Zygros/CONZETIAN-AI/actions/runs/41909782958

The PR remains open and mergeable, but it is not promoted. The PR's own evidence boundary states that the original credential-bearing blob remains in private repository history, provider-side revocation is not verified, and no history rewrite occurred. Those are material security gates, not routine CI failures.

## Federation and evidence boundaries

- This checkpoint is an additive record; no existing repository or architecture node was removed.
- No PR was merged in this cycle.
- No production deployment, real tmux session, payment settlement, Bitcoin/Arweave/OpenTimestamps anchor, or live 26-node federation connection is claimed.
- GitHub skipped external provenance attestation for the private ZYGROS-PRIME repository; no external provenance attestation is claimed.
- The November 3 Termux WAL/checkpoint/OTS source bundle remains unavailable in the connected evidence sources used for this cycle, so its payment and attestation claims remain unreconciled.
- Dropbox was not accessed.

## Reproduction

1. Open the linked PRs and inspect the recorded head commits.
2. Open workflow run 42285809483 and confirm all four matrix jobs and steps.
3. Open workflow run 42107167223 and inspect the token-store and launcher preflight PASS lines.
4. Inspect the CONZETIAN-AI PR #6 workflow runs and the PR's explicit historical-secret/revocation limitations.

This report distinguishes final-head evidence from predecessor-head evidence and fixture tests from production behavior.


## Follow-on reproducibility hardening — final head 2026-11-06

A second review of the newly restored dependency installation identified an opportunity to make the environment itself auditable. The workflow now runs `pip check`, captures `pip freeze --all` for each Python version, and uploads one version-specific environment artifact per matrix job.

- Follow-on commit / final head: `82e3a218a637d2051ff63a8cd1fddcea5b1d4486`.
- Final-head OmniNet Python CI: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42286655494 — success on all four Python versions.
- Each job reported `No broken requirements found.`, `3 passed`, and `Success: no issues found in 11 source files`.
- Four environment artifacts were uploaded with 14-day retention:
  - Python 3.8 artifact 13536904897, SHA-256 `36283adb61c65d80b920e223fdf5cac7f18b62070afd204d8465e57c29f55df3`.
  - Python 3.9 artifact 13538675177, SHA-256 `e1909159a5d8bdcfafda63c6cefec8af73de0fe0a40136ae995737759ee09ca7`.
  - Python 3.10 artifact 13536739998, SHA-256 `59e23955c3a2169f571b482dc799182cdb92f69aa12d41f76c662cea2e99c7dc`.
  - Python 3.11 artifact 13537782407, SHA-256 `9043aab230a310fabccd7fc8b133e95940ad2920a542cd6eb7653515d1c796f6`.
- Final-head Phoenix Audit: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42286655560 — success.
- Final-head Repository Quality Gate: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42286655626 — success.
- Final-head HTC Claim Audit: https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42286655557 — success; artifact 13538405446, SHA-256 `fe35809cac8bc460c72b686224ffb7576d4a266c56307342bf85c22639bf322d`.

These are final-head results for `82e3a218`; they supersede the earlier 8fe5c4e checkpoint for PR #10. The artifacts contain dependency inventories, not credentials or production secrets. Artifact retention is 14 days, so the committed JSON receipt preserves their identifiers and digests after expiration.

The final-head HTC Claim Audit job log reports `claim_count: 10`, `verified: 4`, `refuted: 0`, and `unresolved: 6`. The uploaded artifact digest was printed by the GitHub Actions upload step and matches the artifact metadata returned by GitHub; it was not independently recomputed from downloaded ZIP bytes in this cycle.
