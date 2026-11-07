# 2026-11-07 M.A.I.A. plugin trust-boundary hardening

## Execution result

A review of the current default branch of `Zygros/PHOENIX-PROTOCOL-ULTIMATE` found that `core/phoenix/scripts/maia_framework_orchestrator.py` loaded a caller-supplied path through `importlib.util.spec_from_file_location` without checking that the file came from an approved plugin directory. Importing a Python file executes its top-level code with the orchestrator process's privileges.

A new additive pull request was opened against the active source repository:

- **Source PR:** [PHOENIX-PROTOCOL-ULTIMATE #5](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/pull/5)
- **Branch:** `security/maia-plugin-trust-2026-11-07`
- **Base commit:** `36e571cb869dd2dd1124451109eb8b6acd8873f2`
- **Source head:** `5ee54f4d6b6079aa3b7a6940cadec0667df15518`
- **Tested pull-request merge commit:** `454703e9dbc860426e4ddd453a41e558e21ddd54`
- **PR state:** open, draft, mergeable, unmerged.

The older mirrored security PR in `CONZETIAN-UNIFIED-INTELLIGANCE` was not modified. This change targets the current source repository directly.

## Implementation

The M.A.I.A. orchestrator now accepts an optional `trusted_plugin_dirs` allowlist while preserving the existing demonstration locations:

- `/home/ubuntu/plugins`
- `./plugins`
- `./maia_plugins`

Before importing a plugin, the loader now:

1. Expands and canonicalizes the requested path with `realpath`.
2. Requires a regular Python `.py` file.
3. Requires the resolved file to be contained in an existing configured trust directory.
4. Uses `os.path.commonpath` rather than string-prefix comparison.
5. Rejects parent traversal, sibling-prefix confusion, and symlinks resolving outside the allowlist.
6. Rejects the filesystem root as a trusted directory and rejects a single string where an iterable of directories is expected.
7. Requires a dictionary manifest with a non-empty string `name` before registration.
8. Removes the temporary module entry from `sys.modules` if import or manifest validation fails.

The loader uses unique module names for imported plugins. The existing PERCEIVE-ORIENT-INTEND-ACT-REFLECT architecture and demonstration plugin path remain intact.

Documentation now explains the trust boundary and its limitations. A focused read-only GitHub Actions workflow compiles the source and runs the regression suite, then uploads a machine-readable evidence receipt, test transcript, and SHA-256 manifest.

## Verification

### Focused plugin security workflow

[MAIA Plugin Trust Tests #42411485237](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42411485237) completed successfully on the pull-request head.

- Python: **3.11.18**
- Python compilation: passed.
- Regression tests: **10 passed**.
- Evidence receipt generation: passed.
- Evidence bundle hashing: passed.
- Artifact upload: passed.

The ten regression cases cover empty paths, filesystem-root trust configuration, invalid manifests, non-Python files, external paths, parent traversal, sibling-prefix confusion, a single-string trust configuration, symlink escape, and successful loading/invocation of a trusted fixture.

### Broader Phoenix Audit

[Phoenix Audit #42411485240](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42411485240) completed successfully.

- Repository Python audit: **29 pytest cases passed**.
- Python compilation: passed.
- Credential-pattern scan: passed.
- Federation contract check: passed (`CROSSCONNECT OK`).
- Node, Go, Rust, and Java steps completed with their documented no-build skips because those build manifests are not present at the repository root.

The corresponding push-triggered runs also passed: [focused workflow #42411480931](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42411480931) and [Phoenix Audit #42411480896](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42411480896).

## Reproducible evidence artifact

The final pull-request run uploaded [artifact 13589777617](https://github.com/Zygros/PHOENIX-PROTOCOL-ULTIMATE/actions/runs/42411485237/artifacts/13589777617), named `maia-plugin-trust-evidence`.

- Size: 2,136 bytes.
- GitHub SHA-256: `1aa293090d347ab3895a63ff498dd3a5ee457439e7ce3321974c9213b4b0b9ea`.
- Retention expiry: 2027-02-05T20:31:45Z.

The ZIP was downloaded independently. Its recalculated SHA-256 matched GitHub's reported digest. The archive contained the test transcript, JSON receipt, and SHA-256 manifest. Both entries in the manifest verified successfully.

The JSON receipt binds the evidence to:
- Source branch head `5ee54f4d6b6079aa3b7a6940cadec0667df15518`.
- Tested PR merge commit `454703e9dbc860426e4ddd453a41e558e21ddd54`.
- Base commit `36e571cb869dd2dd1124451109eb8b6acd8873f2`.
- Workflow run `42411485237`.
- Python 3.11.18 and ten passing tests.

## Security boundary and limitations

This is a path allowlist, **not a sandbox**. An allowed plugin still executes in-process with the orchestrator's privileges. Trusted plugin directories must be writable only by authorized operators. Untrusted or multi-tenant plugins require process/container isolation with reduced OS permissions.

The workflow tests use temporary fixture plugins only. No production plugin was launched, no production deployment occurred, and no external service, paid API, credential, Bitcoin anchor, Arweave anchor, or OpenTimestamps anchor was used.

The PR remains draft/open and unmerged. The default branch has not been changed.

## Related open workstreams rechecked

The current GitHub state still shows these earlier implementation PRs open, mergeable, and unmerged, with their latest returned final-head checks successful:

- [ZYGROS-PRIME #9](https://github.com/Zygros/ZYGROS-PRIME/pull/9): Phoenix/Ghost fail-closed launcher preflight.
- [ZYGROS-PRIME #10](https://github.com/Zygros/ZYGROS-PRIME/pull/10): strict canonical Python CI and dependency snapshots.
- [conzet-sovereign-intelligence #40](https://github.com/Zygros/conzet-sovereign-intelligence/pull/40): safe Termux preflight.

No merge was performed in this cycle.
