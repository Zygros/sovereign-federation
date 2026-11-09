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
