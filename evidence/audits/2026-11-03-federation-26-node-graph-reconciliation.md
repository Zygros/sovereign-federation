# Federation Inventory and Directed-Graph Reconciliation — 2026-11-03

## Result

The canonical `FEDERATION_INDEX.json` already contained **26 repositories (21 public, 5 private)**. The federation's local `.phoenix/CROSSCONNECT.json`, generator, and edge-materialization workflow had drifted at 25 repositories. The generator's hard-coded list produced 600 directed edges and the workflow hard-coded the same count.

PR [#23](https://github.com/Zygros/sovereign-federation/pull/23) aligns the central crossconnect with the 26-node index, makes the generator read the index as its source of truth, and makes CI verify the dynamic `n × (n - 1)` edge count.

## Executed changes

- `.phoenix/CROSSCONNECT.json`: `repositories` now matches the 26 names and order in `FEDERATION_INDEX.json`.
- `scripts/generate_crossconnect_edges.py`: removed the duplicated 25-name constant; validates unique index names and exact crossconnect parity before generating edges.
- `.github/workflows/materialize-federation-edges.yml`: now triggers on index/crossconnect changes and verifies the dynamic edge count, unique ordered pairs, valid endpoints, and absence of self-edges.
- `graph/repository_edges.jsonl`: regenerated from 600 to **650** directed logical edges.

## Verification

| Check | Observed result |
|---|---|
| Canonical repository inventory | 26 total, 21 public, 5 private |
| Crossconnect/index parity | 26 names, exact ordered match |
| Directed graph rows | 650 |
| Unique ordered source-target pairs | 650 |
| Expected pairs | 26 × 25 = 650 |
| Invalid endpoints | 0 |
| Self-edges | 0 |
| Materialize Federation Edges | [Run #41706207456: success](https://github.com/Zygros/sovereign-federation/actions/runs/41706207456) |
| Phoenix Audit | [Run #41706207441: success](https://github.com/Zygros/sovereign-federation/actions/runs/41706207441) |

The materialization log explicitly reports `nodes=26 generated=650 expected=650` and `verified_nodes=26 verified_directed_edges=650`. The audit job completed Python compilation, the 420-agent manifest validator, and the secret-pattern scan successfully.

## Reproducibility anchors

- Canonical index blob: `a23401d76dd85810a966a320ff31cda0591a055f`.
- Source patch commit: `e73b9f2c783ef4528b5a0db18c3f1993db3e29af`.
- Workflow-generated graph commit: `5182258659232048de0f34faf0345479e84e655c`.
- Graph blob: `ca5aee4f7e1492b1debb93171e82c63edd7cd1e4`.
- Crossconnect blob: `af09eb3b5c80681a5cda5e933d46c49dbf9318a7`.

## Scope boundary and remaining propagation

The 650 edges are logical repository relationships, not evidence that 650 live network routes or services are active. The pre-patch scan found 25 repositories with a local `.phoenix/CROSSCONNECT.json`; all 25 had 25 entries and omitted `ZYGNUS-OMNI-REPO`. The new repository itself did not yet contain a local crossconnect file. This PR corrects the central federation copy. Six open, mergeable PRs now propose the 26-node crossconnect correction across the central federation, Phoenix, OMEGA-10, skill lattice, Conzetian method, and sovereign intelligence repositories. Their branch CI checks are green. The initial scan found 25 local crossconnect copies; six are now corrected on proposed branches and **19 existing copies remain stale on `main`**. `ZYGNUS-OMNI-REPO` itself still has no local `.phoenix/CROSSCONNECT.json`. See the companion [Phoenix vertical-slice revalidation](./2026-11-03-phoenix-vertical-slice-revalidation.md) for receipt and benchmark evidence.

No external timestamp, Bitcoin confirmation, Arweave/AO read-back, deployment, or payment settlement is claimed.

## Subsequent core-spine propagation — 2026-11-03

| Repository | PR | Verified CI |
|---|---|---|
| `sovereign-federation` | [#23](https://github.com/Zygros/sovereign-federation/pull/23) | [Materialize #41706207456](https://github.com/Zygros/sovereign-federation/actions/runs/41706207456), [Audit #41706678002](https://github.com/Zygros/sovereign-federation/actions/runs/41706678002) |
| `PHOENIX-PROTOCOL-ULTIMATE` | [#4](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/pull/4) | [Proof Cycle #41708321444](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/41708321444), [Audit #41708321215](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/41708321215) |
| `omega-10` | [#4](https://github.com/Zygros/omega-10/pull/4) | [CI #41707544068](https://github.com/Zygros/omega-10/actions/runs/41707544068), [Audit #41707544064](https://github.com/Zygros/omega-10/actions/runs/41707544064) |
| `conzetian-skill-lattice` | [#4](https://github.com/Zygros/conzetian-skill-lattice/pull/4) | [Audit #41706798149](https://github.com/Zygros/conzetian-skill-lattice/actions/runs/41706798149) |
| `conzetian-method` | [#1](https://github.com/Zygros/conzetian-method/pull/1) | [Protocol CI #41706847209](https://github.com/Zygros/conzetian-method/actions/runs/41706847209), [Audit #41706847020](https://github.com/Zygros/conzetian-method/actions/runs/41706847020) |
| `conzet-sovereign-intelligence` | [#39](https://github.com/Zygros/conzet-sovereign-intelligence/pull/39) | [OmniNet CI #41706879903](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/41706879903), [Audit #41706879809](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/41706879809) |

The prior 2026-10-25 cross-link drift is no longer open: the current `docs/CROSS_LINKS.md` on `main` contains PR #34, PR #6, and the Scout reference; both PRs remain merged with the recorded merge commits.
## Post-merge propagation update — 2026-11-03

The six core-spine crossconnect PRs are now merged. The remaining 19 existing manifests were updated on their default branches, and a new `.phoenix/CROSSCONNECT.json` was created in `ZYGNUS-OMNI-REPO`. A fresh read-back of all 26 repositories confirms that every roster exactly matches the canonical ordered 26-node index. The central graph remains 650 unique directed logical edges. Full commit and CI evidence is recorded in [the federation propagation and receipt-hardening report](2026-11-03-federation-propagation-and-receipt-hardening.md).
