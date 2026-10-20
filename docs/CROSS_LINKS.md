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

- **Pull request:** https://github.com/Zygros/omega-10/pull/1
- **Verified code commit:** `188064b3eea6f2df42a30afb695de359b63a6424`
- **Evidence note:** https://github.com/Zygros/omega-10/blob/conzetian/scout-duplicate-evidence-2026-10-19/evidence/audits/2026-10-20-phoenix-recovery-hardening.md
- **CI run 35:** https://github.com/Zygros/omega-10/actions/runs/39461811915
- **Phoenix Audit run 59:** https://github.com/Zygros/omega-10/actions/runs/39461811776

The verified code change hardens local recovery against journal path injection, detects concurrent journal changes, ensures a nonzero corruption fraction exercises recovery, and expands CI lint to all repository Python files. CI passed on Python 3.11 and 3.12 with strict `ruff check .` and pytest. The audit workflow completed its configured checks.

**Evidence boundary:** the Phoenix benchmark remains a local deterministic fixture, not a production recovery service. The pull request is still open and unmerged. These links document code and workflow evidence, not OTS receipt verification or credential remediation.
