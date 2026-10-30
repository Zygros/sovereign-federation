"""Deterministic Omega mesh reference model.

This module is a local test harness, not a production network node. HMAC identities
are used only to make protocol tests deterministic with the Python standard library.
Production deployments must replace this adapter with audited asymmetric signatures
(e.g. Ed25519), protected local key storage, authenticated transport, and policy gates.
"""
from __future__ import annotations

import hashlib
import hmac
import json
from dataclasses import dataclass
from typing import Any, Callable, Iterable


class ProtocolError(ValueError):
    """An input failed a protocol or trust-boundary check."""


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


@dataclass(frozen=True)
class Envelope:
    event_id: str
    issuer: str
    schema_version: int
    created_at: int
    payload: dict[str, Any]
    payload_sha256: str
    signature: str


class DeterministicIdentity:
    """Deterministic test-only signer; never use shared HMAC keys as mesh identities."""

    def __init__(self, node_id: str, secret: bytes) -> None:
        if not node_id or not secret:
            raise ProtocolError("node_id and test secret are required")
        self.node_id = node_id
        self._secret = secret

    def sign(self, body: dict[str, Any]) -> str:
        return hmac.new(self._secret, canonical_json(body), hashlib.sha256).hexdigest()

    def envelope(self, event_id: str, payload: dict[str, Any], created_at: int = 1) -> Envelope:
        payload_hash = digest(payload)
        body = {
            "event_id": event_id, "issuer": self.node_id, "schema_version": 1,
            "created_at": created_at, "payload_sha256": payload_hash,
        }
        return Envelope(**body, payload=payload, signature=self.sign(body))


def verify_envelope(envelope: Envelope, identities: dict[str, DeterministicIdentity], *, now: int, max_age: int = 300) -> None:
    identity = identities.get(envelope.issuer)
    if identity is None:
        raise ProtocolError("unknown issuer")
    if envelope.schema_version != 1:
        raise ProtocolError("unsupported schema version")
    if not envelope.event_id or envelope.created_at > now or now - envelope.created_at > max_age:
        raise ProtocolError("invalid or stale event")
    if digest(envelope.payload) != envelope.payload_sha256:
        raise ProtocolError("payload digest mismatch")
    body = {
        "event_id": envelope.event_id, "issuer": envelope.issuer,
        "schema_version": envelope.schema_version, "created_at": envelope.created_at,
        "payload_sha256": envelope.payload_sha256,
    }
    expected = identity.sign(body)
    if not hmac.compare_digest(expected, envelope.signature):
        raise ProtocolError("signature mismatch")


class AppendOnlyLedger:
    """In-memory hash chain. Integrity-evident for tests, not durable storage."""

    def __init__(self) -> None:
        self._records: list[dict[str, Any]] = []

    def append(self, event: dict[str, Any]) -> dict[str, Any]:
        previous = self._records[-1]["record_sha256"] if self._records else "0" * 64
        record = {"sequence": len(self._records), "previous_sha256": previous, "event": event}
        record["record_sha256"] = digest(record)
        self._records.append(record)
        return dict(record)

    def records(self) -> tuple[dict[str, Any], ...]:
        return tuple(dict(record) for record in self._records)

    def verify(self) -> bool:
        previous = "0" * 64
        for index, record in enumerate(self._records):
            if record["sequence"] != index or record["previous_sha256"] != previous:
                return False
            body = {key: value for key, value in record.items() if key != "record_sha256"}
            if digest(body) != record["record_sha256"]:
                return False
            previous = record["record_sha256"]
        return True


def decide_quorum(
    proposals: Iterable[tuple[str, str]],
    *, expected_nodes: set[str], quorum: int,
    verifier: Callable[[str], bool],
) -> str:
    """Return a proposal only with unique expected voters, quorum, and independent verification."""
    votes = list(proposals)
    voters = [node for node, _ in votes]
    if len(voters) != len(set(voters)):
        raise ProtocolError("duplicate voter")
    if any(node not in expected_nodes for node in voters):
        raise ProtocolError("unexpected voter")
    if quorum < 1 or quorum > len(expected_nodes):
        raise ProtocolError("invalid quorum")
    if len(votes) < quorum:
        raise ProtocolError("quorum unavailable")
    counts: dict[str, int] = {}
    for _, proposal in votes:
        counts[proposal] = counts.get(proposal, 0) + 1
    winner, count = max(counts.items(), key=lambda item: (item[1], item[0]))
    if count < quorum:
        raise ProtocolError("no proposal reached quorum")
    if not verifier(winner):
        raise ProtocolError("independent verifier rejected proposal")
    return winner


class IdempotencyGuard:
    """Reject duplicate operation keys to prevent retry-driven repeated effects."""

    def __init__(self) -> None:
        self._seen: set[str] = set()

    def accept_once(self, key: str) -> bool:
        if not key:
            raise ProtocolError("idempotency key is required")
        if key in self._seen:
            return False
        self._seen.add(key)
        return True
