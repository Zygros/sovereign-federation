# Termux preflight safety hardening — 2026-11-06

## Scope

A stale mobile-preflight draft was inspected in `Zygros/conzet-sovereign-intelligence`. Its branch was 40 commits behind current `main` and diverged. The old PR #29 was left unchanged. A clean branch was created from current `main` and the safe preflight was ported with regression coverage.

## Safety issue found in the older draft

The original `scripts/termux_preflight.sh` on the October 20 branch ran:

`chmod 700 "$PROJECT_DIR" "$PROJECT_DIR/logs" "$PROJECT_DIR/receipts" "$PROJECT_DIR/artifacts"`

Because `PROJECT_DIR` is caller-supplied and may already exist, this would change permissions on an existing user directory. With a path such as `/`, the command could be especially damaging if executed with sufficient privileges. The old draft's static checks did not exercise this permission behavior.

The new implementation does not chmod the caller's base directory or pre-existing directories. It creates a unique per-run directory with `mktemp -d`, then applies mode 0700 only to that newly created run directory and its new child directories.

## Implemented on a clean branch

Repository: https://github.com/Zygros/conzet-sovereign-intelligence

- Branch: `termux-preflight-safety-2026-11-06`
- Final head: `1dc7926b72023472bfbf140e01209813d6739e3f`
- Current-main comparison: 4 commits ahead, 0 behind.
- PR #40: https://github.com/Zygros/conzet-sovereign-intelligence/pull/40
- PR state: open, draft, mergeable, unmerged.
- Changed files: 3; additions: 315; deletions: 0.

Files added:

- `scripts/termux_preflight.sh`
- `scripts/test_termux_preflight.sh`
- `.github/workflows/termux-preflight.yml`

The script remains safe by default: no package installation, network/API calls, repository mutation, agent/service launch, deployment, or paid API use. `--install-prereqs` and `--run-tests` are explicit opt-ins. The evidence report, log, and SHA-256 report manifest are written beneath a unique per-run directory.

## Final-head CI evidence

The first Termux Preflight Safety run failed because the test expected a literal phrase not present in the help text. The failure was inspected in job logs, the assertion was corrected to match the documented help text, and the final head was rerun.

Final branch-push runs:

- Termux Preflight Safety: https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/42287793798 — success.
- Phoenix Audit: https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/42287793547 — success.

Final PR-event runs:

- Termux Preflight Safety: https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/42287950297 — success.
- Phoenix Audit: https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/42287950242 — success.
- OmniNet Python CI: https://github.com/Zygros/conzet-sovereign-intelligence/actions/runs/42287950216 — success across Python 3.8, 3.9, 3.10, and 3.11.

The final Termux Preflight Safety job log records five passing regression groups:

1. Help path is side-effect free.
2. Unknown options are rejected.
3. Default mode does not invoke package installation or pytest, preserves the existing base directory's 0755 mode, creates 0700 per-run directories, and verifies the report checksum.
4. Pytest runs only after explicit opt-in and receives the requested target.
5. Package installation runs only after explicit opt-in; the test intercepts `pkg` with a stub.

## Evidence boundaries

- CI executed on Ubuntu with stubbed `pkg`, `python`, and `pytest`; it did not execute on Android or Termux.
- No package was installed on the user's phone. No phone directory was inspected or modified.
- No agent, service, API, paid endpoint, or deployment was started.
- The tests validate the script's control flow and permission-safety behavior in the mocked environment, not device compatibility or live runtime readiness.
- PR #40 remains a draft for review. PR #29 remains unchanged and unmerged.

## Reproduction

1. Open PR #40 and verify final head `1dc7926b72023472bfbf140e01209813d6739e3f`.
2. Open Termux Preflight Safety run #42287950297 and inspect the five PASS lines.
3. Open Phoenix Audit #42287950242 and OmniNet Python CI #42287950216.
4. Review `scripts/test_termux_preflight.sh`; all package/test side effects are intercepted by stubs.
