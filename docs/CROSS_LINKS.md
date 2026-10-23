# Cross-Repo Links (Canonical Wafer Map)

**Status: ACTIVE_WAFER**  
Always Add. Never replace a repo with another. Every major node should point here, to the skill lattice, and to the evidence substrate.

## Total integration entry point
- [Visibility-aware federation health correction — PR #30](https://github.com/Zygros/conzet-sovereign-intelligence/pull/30) — proposed source fix, regression tests, audit, and explicit CI evidence boundary.
- [Repository visibility audit (branch evidence)](https://github.com/Zygros/conzet-sovereign-intelligence/blob/conzetian/visibility-aware-health-2026-10-22/evidence/audits/2026-10-23-repository-visibility-audit.md) — observed 26-node inventory and public/private split.
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
- ZYGNUS-OMNI-REPO (public): https://github.com/Zygros/ZYGNUS-OMNI-REPO
- Conzet-Intelligence-System- (public): https://github.com/Zygros/Conzet-Intelligence-System-
- ZAAI-SYSTEM: https://github.com/Zygros/ZAAI-SYSTEM
- ZYGROS-PRIME (private): https://github.com/Zygros/ZYGROS-PRIME

## Specialized Nodes (visibility is listed separately below)
- CONZETIAN-UNIFIED-INTELLIGANCE
- CONZETIAN-AI
- Sovereign-Narrative-Intelligence-SNI-
- Conzet-Intelligence-System-

## Integration Rule (Wafer Law)
1. Link. Do not delete.
2. Every major README should point to `sovereign-federation` (map), `conzetian-skill-lattice` (capabilities), and `omega-10` (evidence).
3. New capabilities are added to the skill lattice. New evidence is added to the substrate. The federation index is updated additively.
4. The system is cross-connected like the 50-layer memory tree: every layer knows the others exist.


## Visibility Snapshot — observed 2026-10-23

The connected GitHub inventory returned 26 repositories: 21 public and 5 private. `FEDERATION_INDEX.json` remains the machine-readable node list; all 26 original nodes are preserved.

### Private nodes (5)
- ZYGROS-PRIME: https://github.com/Zygros/ZYGROS-PRIME
- CONZETIAN-UNIFIED-INTELLIGANCE: https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE
- CONZETIAN-AI: https://github.com/Zygros/CONZETIAN-AI
- sovereign-agsi-portal: https://github.com/Zygros/sovereign-agsi-portal
- Sovereign-Narrative-Intelligence-SNI-: https://github.com/Zygros/Sovereign-Narrative-Intelligence-SNI-

This snapshot is a visibility inventory, not proof of repository runtime health. The health-check correction is proposed in [PR #30](https://github.com/Zygros/conzet-sovereign-intelligence/pull/30); its Actions runs must be inspected before the source correction is promoted beyond the tested stage.

## Remote verification checkpoint — observed 2026-10-23

The live GitHub inventory and the proposed machine-readable index were re-compared before this note was added: **26/26 names match exactly, visibility matches for every node, and the index totals 21 public / 5 private**.

### Source correction CI evidence

- The health-check correction is proposed in [conzet-sovereign-intelligence PR #30](https://github.com/Zygros/conzet-sovereign-intelligence/pull/30).
- On source commit [96c04cf](https://github.com/Zygros/conzet-sovereign-intelligence/commit/96c04cf4544d3598ccdd8b5d56a7f33bd879158b), [OmniNet Python CI run #259](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/40012093501) concluded success. The Python 3.8, 3.9, 3.10, and 3.11 matrix jobs each reported **78 passed** in the repository pytest suite and included the three visibility regression cases.
- [Phoenix Audit run #306](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/40012093647) concluded success at the job level, but its Python compile/audit subcheck was skipped after a find/grep broken-pipe result. It is not counted as Python compileall proof.
- Workflow hygiene is not clean: Black reported 89 files needing formatting, including the touched test file, and mypy reported a duplicate conftest module. Those checks are explicitly non-blocking in the workflow. See the [append-only evidence checkpoint](https://github.com/Zygros/conzet-sovereign-intelligence/blob/3604310ba94f74a4ebcb9ada8ed983902ef2d0a6/EVIDENCE_CHAIN.md) and the [2026-10-23 visibility audit](https://github.com/Zygros/conzet-sovereign-intelligence/blob/conzetian/visibility-aware-health-2026-10-22/evidence/audits/2026-10-23-repository-visibility-audit.md).

This records a verified CI result for the cited code commit, not for any later evidence-only branch head. The proposed correction and index reconciliation remain unmerged; mocked regression tests verify denominator behavior, not live reachability of every public URL. No deployment or external timestamp/Bitcoin/Arweave anchor is claimed.

## Phoenix Audit evidence-integrity correction — observed 2026-10-23

- **Source correction:** [conzet-sovereign-intelligence PR #31](https://github.com/Zygros/conzet-sovereign-intelligence/pull/31) changes the Python-source probe in the root Phoenix Audit workflow and three nested copies to stop `find` after the first match.
- **Reproduction:** the old probe falsely reported no Python source on a 5,000-file fixture; the corrected probe detected source. Four local regression assertions passed. The [audit record](https://github.com/Zygros/conzet-sovereign-intelligence/blob/conzetian/fix-phoenix-audit-source-probe-2026-10-23/evidence/audits/2026-10-23-phoenix-audit-source-probe.md) and [append-only evidence chain](https://github.com/Zygros/conzet-sovereign-intelligence/blob/conzetian/fix-phoenix-audit-source-probe-2026-10-23/EVIDENCE_CHAIN.md) preserve the procedure and scope.
- **Remote status at this checkpoint:** PR #31 is open and unmerged; no Actions run for its new head had yet been returned by the connected GitHub run lookup. The correction has not been promoted to `main`, and its full repository audit/test path remains to be verified.

This is an evidence-integrity correction, separate from the visibility-health correction in PR #30. It does not claim deployment, live runtime health, or external anchoring.

## Remote validation follow-up — observed 2026-10-23

- [Phoenix Audit run #317](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/40013680276) completed successfully for PR #31's source commit. Unlike the earlier run, its log shows the corrected early-exit probe proceeded into the Python audit; the root suite reported **79 passed in 0.66s**.
- [OmniNet Python CI run #261](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/40013680033) also completed successfully across Python 3.8, 3.9, 3.10, and 3.11. Each matrix log includes the four probe regression cases.
- The run verifies the PR's source commit, not merged `main`. Repository-wide Black formatting and mypy checks remain non-blocking and report outstanding hygiene issues; they are not recorded as clean.
- Reconciliation was repeated immediately before this append: the proposed `FEDERATION_INDEX.json` matches the connected live inventory at **26/26 exact repository names, 21 public, 5 private**, with zero visibility mismatches or omissions.

PR #31 remains proposed and unmerged. The prior “Actions not yet returned” note records its earlier observation time; this addendum records the later successful runs. No deployment or external anchor is claimed.

## Latest probe-code verification — observed 2026-10-23

- Latest source/test commit: [12e667487b](https://github.com/Zygros/conzet-sovereign-intelligence/commit/12e667487bb2cb0365aeab459d7a40715c83058d).
- [Phoenix Audit run #322](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/40014458363) completed successfully after the corrected probe, executing the root Python audit and reporting **79 passed in 0.69s**.
- [OmniNet Python CI run #263](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/40014458405) completed successfully across Python 3.8, 3.9, 3.10, and 3.11; every matrix job collected and passed the four-case probe regression module.
- Remaining caveat: the repository's non-blocking Black check still flags the new test module, and mypy still reports a duplicate `conftest` module. The Actions runs are green, but formatting/type checking are not reported as clean.
- Live inventory reconciliation repeated before this append: **26/26 exact repository names; 21 public; 5 private; zero visibility mismatches and zero omissions**. This confirms the proposed index data, not live URL reachability or merge state.

The newest verification is an additive follow-up to the earlier run #320 checkpoint. PR #31 remains open and unmerged.


## Post-merge Federation Health verification — observed 2026-10-23

This addendum supersedes only earlier status statements above that describe the visibility-health source correction as proposed or unmerged. Those entries remain preserved as time-accurate historical checkpoints.

- **Source correction merged:** [merge commit 83bd1854](https://github.com/Zygros/conzet-sovereign-intelligence/commit/83bd18545e5614987017088677321a1508530313). The merged [health-check script](https://github.com/Zygros/conzet-sovereign-intelligence/blob/83bd18545e5614987017088677321a1508530313/scripts/federation_check.py) uses separate `PUBLIC_REPOS` and `PRIVATE_REPOS` lists and retains `REPOS` as a compatibility alias for the public roster.
- **Live Federation Health run:** [run 40016844465](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/40016844465) completed with `success` for source commit `83bd18545e5614987017088677321a1508530313`. Its published [2026-10-23 health report](https://github.com/Zygros/conzet-sovereign-intelligence/blob/federation-health/health/2026-10-23.txt) records **21/21 public repository URLs responding HTTP 200**; the [run metadata](https://github.com/Zygros/conzet-sovereign-intelligence/blob/federation-health/health/RUN_META_2026-10-23.yaml) binds the artifact to that source commit and run URL.
- **Post-merge code checks:** [OmniNet Python CI run 40016844582](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/40016844582) completed successfully, with Python 3.8, 3.9, 3.10 and 3.11 jobs passing. [Phoenix Audit run 40016844576](https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/40016844576) also completed successfully.
- **Inventory basis:** the connected GitHub inventory observed on 2026-10-23 contained 26 repositories, 21 public and 5 private. The separate machine-readable index reconciliation remains tracked in this PR's visibility-index changes.

**Evidence boundary:** HTTP 200 establishes public URL reachability at the run time, not correctness of repository contents, deployed Conzetian/Phoenix runtime health, third-party reproduction, or Bitcoin/Arweave anchoring. The separate Phoenix Audit probe correction remains an independent PR and is not represented as merged by this checkpoint.
