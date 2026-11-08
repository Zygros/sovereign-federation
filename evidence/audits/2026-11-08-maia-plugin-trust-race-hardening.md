# M.A.I.A. Plugin Trust Hardening and Mirror Propagation

**Recorded:** 2026-11-08  
**Scope:** Active Phoenix implementation plus four repository-mirror copies  
**State:** Code and CI changes are on open pull-request branches; neither source PR was merged.

## Executive result

The active M.A.I.A. plugin loader was hardened against group/world-writable trust locations, pathname replacement between validation and import, duplicate plugin-name replacement, and loss of module source-location metadata. The same security implementation was then propagated to four byte-identical M.A.I.A. orchestrator copies in the Conzetian unified repository.

Both focused regression workflows passed. Their evidence ZIPs were downloaded and independently checked against GitHub's reported SHA-256 digests; each ZIP's internal SHA-256 manifest also matched its contained files.

## 1. Active Phoenix source

Repository: [PHOENIX-PROTOCOL-ULTIMATE](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE)  
PR: [#5 — M.A.I.A. trusted plugin loading](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/pull/5)  
Branch: \`security/maia-plugin-trust-2026-11-07\`  
Source head: \`e4312edd3a55c8dad64832ba592a596f75bf113e\`  
Base: \`36e571cb869dd2dd1124451109eb8b6acd8873f2\`  
Tested pull-request merge commit: \`33baf707eaf3f89988b7e3395648eeab46f7064d\`

### Implementation

The orchestrator now:

- Requires the configured trusted root and each descendant directory to be non-writable by group/other.
- Requires the plugin file to be a regular file and non-writable by group/other.
- Opens the resolved file with no-follow semantics where supported.
- Compares the opened descriptor's device/inode with the current path entry and rejects detected replacement.
- Revalidates containment and path permissions after open.
- Reads and compiles the exact bytes obtained through the opened descriptor instead of asking an import loader to reopen the pathname.
- Checks file identity, size, modification time, and change time before/after reading.
- Rejects duplicate plugin names rather than replacing an existing registry entry.
- Preserves module \`__file__\` metadata for plugins that resolve resources relative to their source file.

The existing M.A.I.A. PERCEIVE → ORIENT → INTEND → ACT → REFLECT structure and demonstration trust-directory defaults remain in place.

### Verification

- [Focused MAIA Plugin Trust Tests #42520602862](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42520602862): **15/15 unittest cases passed** on Python 3.11.18. Compilation, receipt generation, evidence hashing, and artifact upload all succeeded.
- [Phoenix Audit #42520602858](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42520602858): **34 pytest cases passed**, plus compilation, credential-pattern scan, and federation contract checks.
- The first expanded run exposed a malformed escaped-newline fixture in the duplicate-name test. The fixture was corrected in commit \`b3a53656ba23dd7f99628f30ec7dc93f8002b8e5\`; the final PR-head run above passed.

### Artifact

[MAIA plugin trust evidence artifact 13633535138](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42520602862/artifacts/13633535138)

- ZIP size: 2,464 bytes.
- GitHub-reported ZIP SHA-256: \`c94461aa062bdf930dfe4b4b2a9c4e73cb546230ccc14566b554e24e41c6f0dc\`.
- Independent download recalculation: exact match.
- Internal SHA-256 manifest: both listed file digests matched the extracted files.
- Receipt: 15 tests passed; source head and tested merge commit are recorded.
- Retention reported by GitHub: 90 days, expiring 2027-02-06.

PR #5 remains **open, draft, mergeable, and unmerged**. The default branch was not changed.

## 2. Four-copy Conzetian mirror propagation

Repository: [CONZETIAN-UNIFIED-INTELLIGANCE](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE)  
PR: [#5 — M.A.I.A. plugin trust validation across mirrored sources](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/pull/5)  
Branch: \`fix/aikido-security-code-audit-97974299-9wzs\`  
Source head: \`44029fe1e77ff5e82ef0dca3ce439003635e808c\`  
Base: \`3b934e96803f4aef232734e0cfdb1a727ed6084a\`  
Tested pull-request merge commit: \`65317eb029f8924f76a3d0f85be2a11298b8fd8d\`

The same descriptor-bound loader, permissions checks, duplicate-name protection, and module-location behavior were applied to all four copies:

1. \`source-repositories/PHOENIX-PROTOCOL-ULTIMATE/core/phoenix/scripts/maia_framework_orchestrator.py\`
2. \`source-repositories/ZYGROS-PRIME/Phoenix Protocol/maia_framework_orchestrator.py\`
3. \`source-repositories/ZYGROS-PRIME/Phoenix Protocol/maia_framework_orchestrator_1.py\`
4. \`source-repositories/conzet-sovereign-intelligence/scripts/maia_framework_orchestrator.py\`

All four files have the same Git blob SHA, \`bf9260c5f10324baffd33fdde6fb310866bfb2c0\`, and the workflow independently checked byte-for-byte equality.

### Verification

- [MAIA Mirror Plugin Trust Tests #42520998188](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42520998188): **6 unittest methods passed**, including 20 per-mirror security-case executions across the four copies and one byte-identical-source check. Python 3.11 compilation passed for all four copies and the test harness.
- [Phoenix Audit #42520998333](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42520998333): **19 pytest tests and 23 subtests passed**; source-discovery probes and credential-pattern scan passed.
- [Conzetian Contract Verification #42520998127](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42520998127): passed.
- [Phoenix API Key Policy #42520998470](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42520998470): passed.

### Artifact

[MAIA mirror plugin trust evidence artifact 13633034237](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42520998188/artifacts/13633034237)

- ZIP size: 2,431 bytes.
- GitHub-reported ZIP SHA-256: \`65a5d2e7fc2fa52db70969ff8c5a9b8521b79437b7fd9386d676cc929bf6f7b3\`.
- Independent download recalculation: exact match.
- Internal SHA-256 manifest: both listed file digests matched the extracted files.
- Receipt records four mirrors, 20 per-mirror security-case executions, six unittest methods, Python 3.11.18, source head, and tested merge commit.
- Retention reported by GitHub: 90 days, expiring 2027-02-06.

PR #5 remains **open, non-draft, mergeable, and unmerged**. The unified repository default branch was not changed.

## 3. Security boundary and non-claims

These changes establish a stricter in-process plugin allowlist and reduce pathname-replacement exposure. They do not sandbox plugins. A trusted plugin still executes with the orchestrator's privileges. The checks do not isolate processes sharing the same operating-system identity; trusted directories and files must remain writable only by authorized operators.

All new execution evidence comes from GitHub-hosted Linux runners and test fixtures. No plugin was launched against a production system, no Android/Termux files or permissions were changed, no paid endpoint or external credential was used, and no external Bitcoin, Arweave, or OpenTimestamps anchor was created.

The two PRs are deliberately left unmerged. Mergeability is not the same as review approval or production deployment.
