# M.A.I.A. plugin trust-root ancestor hardening and Phoenix receipt revalidation

Date: 2026-11-09

## Finding reproduced

The original M.A.I.A. plugin loader validated the configured trust root and descendants but did not validate directories above the trust root. A trust root located under a group/world-writable, non-sticky parent could be renamed and replaced while retaining the same configured pathname. The replacement root and plugin could both use restrictive mode bits, yet the loader accepted and executed the replacement plugin.

A local A/B reproduction confirmed the behavior:

- Pre-patch: parent mode `0777` without sticky bit, trust root `0755`, plugin `0644`; the replacement plugin was accepted and its top-level marker code executed.
- Patched: the same replacement was rejected; the marker was not created.

## Implemented hardening

The fix was applied additively to the existing public Phoenix security PR and its four mirrored copies.

### Public Phoenix implementation

- Repository: [PHOENIX-PROTOCOL-ULTIMATE](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE)
- Existing PR: [#5 security(maia): restrict plugin imports to trusted directories](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/pull/5)
- Branch: `security/maia-plugin-trust-2026-11-07`
- Final head: `6b1fee053e6fa4e275c06e06da28b84d88ed5ed0`
- Changes: validate the configured trust-root owner (service UID or root on POSIX), inspect the complete ancestor chain to filesystem root, reject group/other-writable ancestors unless the sticky bit prevents other users from replacing children, and add a replacement regression test plus documentation.

Verification:

- [MAIA Plugin Trust Tests run #42690528185](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42690528185): success, 16 tests on Python 3.11.18.
- [Phoenix Audit run #42690528182](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42690528182): success.
- Evidence artifact ID: `13707126233`.
- Artifact SHA-256: `10eeaddf61a0ffe22244a15e81d4f338ef77f65edb5c77d203270313e6ba24aa`; the downloaded ZIP hash matched GitHub's digest.

### Four mirrored implementations

The same hardening was propagated to all four byte-identical copies in [CONZETIAN-UNIFIED-INTELLIGANCE PR #5](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/pull/5):

- Branch: `fix/aikido-security-code-audit-97974299-9wzs`
- Final head: `6f750ed0c9c1a0242e1596d64e51fdc1942e914d`
- Updated: all four mirrored orchestrator files, the shared mirror regression suite, and trust-boundary documentation.
- [MAIA Mirror Plugin Trust Tests run #42690914349](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42690914349): success, 7 unittest methods, 20 per-mirror security-case executions across 4 mirrors, Python 3.11.18.
- Evidence artifact ID: `13707635524`.
- Artifact SHA-256: `8839c20ca2ba9458ca3b0752added11483cdf785212fecdd6418916bf468e386`; the downloaded ZIP hash matched GitHub's digest.

## Phoenix proof-cycle receipt revalidation

The existing post-merge Proof Cycle run [#41711973409](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/41711973409) on commit `4b91814f906ea7943625544958c88d9cb8f0aea7` was downloaded and independently revalidated.

- Artifact ID: `13268034674`.
- Artifact SHA-256: `791dd30271db389eadfcfd2642e59f12bfdb15a5374bdd797fc77dc49be0c666`; the downloaded ZIP hash matched GitHub's digest.
- Local checks: 8 proof-runner self-tests and 15 independent receipt-contract tests passed.
- All three receipts verified: `PASS` (4 events), `REPAIRED` (6 events), and `FAIL` (4 events).
- All five external-evidence flags were false in every receipt: external AI, web research, Bitcoin anchor, Arweave anchor, and OpenTimestamps anchor.

This verifies the deterministic local proof machinery, tamper detection, repair/failure handling, and explicit evidence boundaries. It does not establish external AI execution, live web research, external anchoring, deployment, or live federation connectivity.

## Execution boundaries

Both M.A.I.A. PRs remain open and unmerged. No production deployment or external anchor was performed. The changes are reviewable branch commits with successful CI evidence, not a claim of production activation.

A reproducible local evidence bundle was also preserved in the conversation runtime; its SHA-256 is `08f749a06bb43cc91ea48a8815fa7c9e6fe717500c8a1bb4fc297c3e7b5d1a9f`.


## M.A.I.A. untrusted-owner boundary closure — 2026-11-10

The follow-up review closed the P1 owner-trust gap across the three existing security branches without renaming the M.A.I.A. orchestrators or changing the runtime architecture. On POSIX, plugin files, descendant directories, configured roots, and every ancestor now require ownership by root or the effective service UID. Sticky writable ancestors are allowed only when their owner is trusted. The loader also checks descriptor ownership with fstat(), compares it with path metadata, and rechecks after reading.

- **ZYGROS-PRIME PR #11** — branch `security/maia-plugin-trust-root-chain-2026-11-09`, head `69ae91e3a73e3eb5f4a522ed2d843d0254c2afc6`. [MAIA Plugin Trust Tests run #42899478288](https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42899478288) passed 8 unittest methods on Python 3.11.18; [HTC Claim Audit #42899478326](https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42899478326), [Phoenix Audit #42899478416](https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42899478416), [Repository Quality Gate #42899478190](https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42899478190), and [OmniNet Python CI #42899478872](https://github.com/Zygros/ZYGROS-PRIME/actions/runs/42899478872) also succeeded. Artifact 13803010367 ZIP SHA-256: `bea515871ec63e0e252543b798230e1287ba1fc831f5dcd664314c937142e8c1`; its canonical receipt self-hash was independently recomputed and matched. The P1 review thread and the related medium-severity ownership thread were both resolved after the passing focused workflow.
- **PHOENIX-PROTOCOL-ULTIMATE PR #5** — branch `security/maia-plugin-trust-2026-11-07`, head `801f321e1a6831a178237c0271532bb710b506b8`. [MAIA Plugin Trust Tests #42899611987](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42899611987) passed 17 unittest methods on Python 3.11.18; [Phoenix Audit #42899610112](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42899610112) succeeded. Artifact 13802666114 ZIP SHA-256: `d8aba14893de54e9aa0f831a3d8d3003e2e92d054dbd5aaae2dab23305957b29`; both entries in its internal SHA-256 manifest matched.
- **CONZETIAN-UNIFIED-INTELLIGANCE PR #5** — branch `fix/aikido-security-code-audit-97974299-9wzs`, head `81d344cb0baff9ac951550a6293681e10dada483`. All four preserved orchestrator copies were updated identically. [MAIA Mirror Plugin Trust Tests #42899722312](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42899722312) passed 8 unittest methods across the four copies; [Phoenix Audit #42899722330](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42899722330), [Phoenix API Key Policy #42899722346](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42899722346), and [Conzetian Contract Verification #42899722249](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42899722249) also succeeded. Artifact 13802746276 ZIP SHA-256: `d97d22a9f52b00868ecea331808b0aa4de3cd64f27f583ee130d569b077edaf7`; both entries in its internal SHA-256 manifest matched.

**Promotion boundary:** all three source PRs remain open and unmerged. Their default branches were not changed. The runs verify the hosted branch code and regression suites; they do not establish production deployment, live Android/Termux operation, external anchoring, or live federation connectivity.
