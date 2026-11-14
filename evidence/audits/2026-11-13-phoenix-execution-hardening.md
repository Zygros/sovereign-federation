# Conzetian/Phoenix execution hardening — 2026-11-13/14

This append-only receipt records three branch-level changes.

## Termux preflight

- Source: [conzet-sovereign-intelligence PR #40](https://github.com/Zygros/conzet-sovereign-intelligence/pull/40)
- Head: `459e7b3ab1d92cc2f8e2214c71a5eb7e89b9ee54`
- Missing `pkg`, failed update, and failed install are captured after the evidence run initializes.
- Focused workflow 43535804461: success. At recording time, Phoenix Audit 43535804460 and OmniNet CI 43535804475 were in progress.

## M.A.I.A. duplicate registration

- Source: [conzet-sovereign-intelligence PR #41](https://github.com/Zygros/conzet-sovereign-intelligence/pull/41)
- Head: `be8a832ef4a77f0b074311867ff91720e444c06c`
- Duplicate plugin manifest names are rejected without replacing the first registered module.
- The first hosted focused run failed because the new test fixture wrote literal backslash-n sequences into its temporary plugin source (16 passed, 1 failed). The fixture was corrected in follow-up commit `be8a832ef4a77f0b074311867ff91720e444c06c`; a new hosted run for that corrected head had not yet appeared in the workflow read-back.

## A17 restore guard

- Source: [phoenix-survival-backup PR #1](https://github.com/Zygros/phoenix-survival-backup/pull/1)
- Head: `631b3a0311cab3851a237206f8d19f75f385162a`
- Missing/malformed memory telemetry aborts. Restore output without a matching manifest SHA is marked unverified and returns exit 3.
- No A17 device execution. Current device state remains unknown.

## Boundary

All three PRs are open and unmerged. No deployment, device execution, external anchor, payment, or live mesh connection is claimed.
