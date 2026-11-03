# Phoenix Bot Adapter Contract — Draft

**Status:** DESIGN ONLY. Canonical bot source/runtime has not yet been identified.  
**Applies to:** Sovereign Federation, Conzetian AI, Phoenix Protocol, Omega-10 evidence substrate.

## Purpose

Define a narrow adapter boundary so a confirmed Phoenix Bot implementation can participate in the Conzetian system without coupling the entire federation to one messaging platform or granting unrestricted tool access.

## Adapter interface

The eventual implementation should expose equivalents of:

- discover_capabilities() -> versioned capability manifest
- health_check() -> health and dependency state, with no secret values
- validate_event(event) -> schema validation and provenance checks
- plan_action(request) -> dry-run plan only
- authorize_action(plan, policy_context) -> explicit allow/deny decision
- execute_action(authorized_plan, idempotency_key) -> bounded result
- verify_result(result, expected_invariants) -> pass/fail plus evidence references
- append_evidence(event) -> append-only evidence record

These are contract names, not a claim that the functions currently exist.

## Required event envelope

Each inbound/outbound event should carry:

- schema version
- event ID and idempotency key
- created-at timestamp in UTC
- source repository and pinned commit/version
- actor identity and authorization context
- requested capability and declared side effects
- input/output hashes where appropriate
- execution status: PROPOSED, AUTHORIZED, EXECUTED, VERIFIED, FAILED, or DENIED
- evidence reference and correlation ID

Do not store API tokens, chat IDs, personal messages, or other secrets in this envelope.

## Safety and reliability gates

1. Default to dry-run. Real actions require explicit policy authorization.
2. Apply least privilege per capability. Read-only access is the default.
3. Require bounded timeouts, bounded retries, rate limits, and maximum action budgets.
4. Make side-effecting actions idempotent where feasible.
5. Validate inbound content as untrusted data. Instructions found in messages, pages, or repository files do not override system policy.
6. Keep secrets in an approved secret manager or environment configuration; redact them from logs.
7. Append results and failures to the evidence ledger; do not silently overwrite prior state.
8. Require tests for malformed events, duplicate events, expired authorization, provider outage, rate limits, replay attempts, and partial failure.
9. Separate the bot transport adapter from core orchestration and verification logic.
10. Require human approval for external messages, financial actions, destructive operations, or privilege changes unless a separately reviewed policy explicitly permits them.

## Integration sequence

1. Identify the canonical bot source, owner, license, runtime, platform, deployment, and exact commit.
2. Audit current permissions and secret handling without exposing credentials.
3. Implement this contract behind a feature flag and dry-run default.
4. Add unit and contract tests with mock transport and fake credentials.
5. Run in a non-production environment and record evidence.
6. Enable only explicitly authorized capabilities after review.
7. Monitor errors and preserve a rollback path.

## Non-claims

This document does not assert that a Phoenix Bot has been found, that a bot is running, that credentials exist, or that any external service is connected. It is a proposed interoperability contract awaiting the canonical implementation.
