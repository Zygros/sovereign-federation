# Cross-Repo Links (Canonical Wafer Map)

**Status: ACTIVE_WAFER**  
Always Add. Never replace a repo with another. Every major node should point here, to the skill lattice, and to the evidence substrate.

## Total integration entry point
- [Sovereign Conzetian Total Integration Index (2026-10-16)](SOVEREIGN_CONZETIAN_TOTAL_INTEGRATION_2026-10-16.md) — Phoenix Ω∞ × NYXAVEN × AVEN × Ω-PRIME × Memoria Omnia × HTC × Cloud/API lattice; evidence classes, security gates and staged execution plan.

## Core Nodes (the wafer spine)
- **Federation map**: https://github.com/Zygros/sovereign-federation
- **Capability wafer (Skill Lattice)**: https://github.com/Zygros/conzetian-skill-lattice
- **Evidence substrate**: https://github.com/Zygros/omega-10
- **Method framework**: https://github.com/Zygros/conzetian-method

## Phoenix family
- Meta-unified: https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE
- SSI (JS): https://github.com/Zygros/ultimate-phoenix-protocol-ssi
- Python line: https://github.com/Zygros/ultimate-phoenix-protocol
- Convergence bridge: https://github.com/Zygros/multi-ai-convergence-protocol
- CSI narrative: https://github.com/Zygros/conzet-sovereign-intelligence

## Architecture & Routing
- omninet-v4: https://github.com/Zygros/omninet-v4
- CZAOUA: https://github.com/Zygros/CZAOUA-UNITY-SYSTEM
- we-omega: https://github.com/Zygros/we-omega

## Interfaces
- zyth-ultimate: https://github.com/Zygros/zyth-ultimate
- Portal (private): https://github.com/Zygros/sovereign-agsi-portal

## Archives & Lineage
- AGSI Archive: https://github.com/Zygros/Sovereign-AGSI-Archive
- Grossian_Scrolls: https://github.com/Zygros/Grossian_Scrolls
- ZAAI-SYSTEM: https://github.com/Zygros/ZAAI-SYSTEM
- ZYGROS-PRIME: https://github.com/Zygros/ZYGROS-PRIME

## Private / Specialized
- CONZETIAN-UNIFIED-INTELLIGANCE
- CONZETIAN-AI
- Sovereign-Narrative-Intelligence-SNI-
- Conzet-Intelligence-System-

## Integration Rule (Wafer Law)
1. Link. Do not delete.
2. Every major README should point to `sovereign-federation` (map), `conzetian-skill-lattice` (capabilities), and `omega-10` (evidence).
3. New capabilities are added to the skill lattice. New evidence is added to the substrate. The federation index is updated additively.
4. The system is cross-connected like the 50-layer memory tree: every layer knows the others exist.

## Phoenix Recovery Hardening — 2026-10-20

- **Review PR:** https://github.com/Zygros/omega-10/pull/1
- **Current reviewed code commit:** `e0767e8fb50eeac531872130f40c30117f864e2a`
- **Evidence note:** https://github.com/Zygros/omega-10/blob/conzetian/scout-duplicate-evidence-2026-10-19/evidence/audits/2026-10-20-phoenix-recovery-hardening.md
- **CI run 37:** https://github.com/Zygros/omega-10/actions/runs/39462417459
- **Phoenix Audit run 63:** https://github.com/Zygros/omega-10/actions/runs/39462417954

The latest recorded CI run passed on Python 3.11 and 3.12 with strict `ruff check .` and pytest; Phoenix Audit run 63 completed successfully. The code hardens the local recovery fixture against journal path injection, detects concurrent journal changes, ensures nonzero corruption fractions exercise recovery, and expands lint to repository-wide Python files.

**Evidence boundary:** this is a local deterministic benchmark, not a production recovery service. PR #1 remains open and unmerged. These links do not establish OTS receipt verification or credential remediation.

## OpenTimestamps Inventory Reconciliation — 2026-10-20

- **Evidence note:** https://github.com/Zygros/omega-10/blob/conzetian/scout-duplicate-evidence-2026-10-19/evidence/audits/2026-10-20-ots-inventory-reconciliation.md
- **Completed Dropbox inventory:** 1,770 entries across 3 fully consumed pages; 260 files ending in `.ots`, 260 unique paths, and no duplicate basenames.
- **Known placeholder candidate:** `/Download11.8.25/DAO_Proposal_Scroll476.ots`, 74 bytes; Dropbox text extraction returned `OpenTimestamps placeholder`.
- **Evidence boundary:** the earlier 261 count remains unreconciled; the 260 inventory count is confirmed by two complete scans. No OTS receipt was cryptographically verified and no Bitcoin confirmation is claimed.
- **Federation review PR:** https://github.com/Zygros/sovereign-federation/pull/4

This cross-link is now open for review in PR #4; it has not been merged.

## Execution Checkpoint — 2026-10-20

- **Cross-repository execution evidence:** https://github.com/Zygros/omega-10/blob/conzetian/scout-duplicate-evidence-2026-10-19/evidence/audits/2026-10-20-phoenix-federation-execution-checkpoint.md
- **Federation review PR:** https://github.com/Zygros/sovereign-federation/pull/4

The checkpoint records the observed Phoenix CI/Phoenix Audit results, federation PR creation, updated cross-link commit, and remaining verification boundaries. It explicitly distinguishes the earlier queued workflow run from a verified run on the latest federation commit.
