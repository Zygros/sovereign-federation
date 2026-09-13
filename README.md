# Sovereign Federation — ACTIVE_WAFER v0.2

**Always Add · Never Take · Zero Friction**

**Status:** ACTIVE_WAFER

Additive unification layer over all Zygros / Conzetian repositories.

This is not a monorepo merge.  
This is a cross-connected wafer: every major node points to the others so the system can be entered from any door and still find the whole architecture.

## Core Nodes (the spine)

| Role | Repository |
|------|------------|
| Federation map / index | [sovereign-federation](https://github.com/Zygros/sovereign-federation) |
| Capability wafer (Skill Lattice) | [conzetian-skill-lattice](https://github.com/Zygros/conzetian-skill-lattice) |
| Evidence substrate | [omega-10](https://github.com/Zygros/omega-10) |
| Method framework | [conzetian-method](https://github.com/Zygros/conzetian-method) |

## What this federation does

- Maintains a machine-readable inventory of all related repositories (`FEDERATION_INDEX.json`)
- Publishes canonical cross-links (`docs/CROSS_LINKS.md`)
- Treats the skill lattice as the living capability layer
- Treats omega-10 as the shared evidence / ledger / recovery layer
- Never deletes, archives, or rewrites history of member repositories

## Wafer Principle

Every major repository should point back to:
1. this federation (map)
2. the skill lattice (capabilities)
3. omega-10 (evidence)

The system is cross-connected like the 50-layer memory tree: every layer knows the others exist.

## Key files

- `FEDERATION_INDEX.json` — full repo inventory + core nodes + invariants
- `docs/CROSS_LINKS.md` — canonical wafer map
- `FEDERATION_SPINE.md` — four-center resilience view
- `capabilities/`, `protocols/`, `gaps/`, `mcp/` — supporting matrices

## Invariants

1. No repository is deleted or archived by this federation.
2. No history is rewritten.
3. Claims remain DESIGNED until executable evidence is linked.
4. Unification is index + shared substrate + bidirectional links, not replacement.
5. Always Add. Never Take.

## License

MIT — see `LICENSE`.
