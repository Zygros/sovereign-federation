from dataclasses import replace

import pytest

from omega_mesh.reference_node import (
    AppendOnlyLedger,
    IdempotencyGuard,
    ProtocolError,
    DeterministicIdentity,
    decide_quorum,
    verify_envelope,
)


def identities():
    nodes = {
        "node-a": DeterministicIdentity("node-a", b"test-key-a"),
        "node-b": DeterministicIdentity("node-b", b"test-key-b"),
        "node-c": DeterministicIdentity("node-c", b"test-key-c"),
    }
    return nodes


def test_valid_envelope_verifies():
    keys = identities()
    envelope = keys["node-a"].envelope("event-1", {"action": "dry-run"}, created_at=100)
    verify_envelope(envelope, keys, now=101)


def test_payload_tampering_is_rejected():
    keys = identities()
    envelope = keys["node-a"].envelope("event-1", {"action": "dry-run"}, created_at=100)
    tampered = replace(envelope, payload={"action": "execute"})
    with pytest.raises(ProtocolError, match="payload digest mismatch"):
        verify_envelope(tampered, keys, now=101)


def test_unknown_issuer_and_stale_event_are_rejected():
    keys = identities()
    envelope = keys["node-a"].envelope("event-1", {"x": 1}, created_at=100)
    with pytest.raises(ProtocolError, match="unknown issuer"):
        verify_envelope(envelope, {}, now=101)
    with pytest.raises(ProtocolError, match="stale"):
        verify_envelope(envelope, keys, now=1000, max_age=10)


def test_hash_chain_detects_record_mutation():
    ledger = AppendOnlyLedger()
    ledger.append({"type": "proposal", "value": "A"})
    ledger.append({"type": "decision", "value": "A"})
    assert ledger.verify()
    internal = ledger._records
    internal[0]["event"]["value"] = "FORGED"
    assert not ledger.verify()


def test_three_node_quorum_requires_verifier_approval():
    nodes = {"node-a", "node-b", "node-c"}
    assert decide_quorum(
        [("node-a", "A"), ("node-b", "A"), ("node-c", "B")],
        expected_nodes=nodes, quorum=2, verifier=lambda proposal: proposal == "A",
    ) == "A"
    with pytest.raises(ProtocolError, match="verifier rejected"):
        decide_quorum(
            [("node-a", "A"), ("node-b", "A")],
            expected_nodes=nodes, quorum=2, verifier=lambda proposal: False,
        )


def test_quorum_loss_duplicate_and_unknown_voter_fail_closed():
    nodes = {"node-a", "node-b", "node-c"}
    with pytest.raises(ProtocolError, match="quorum unavailable"):
        decide_quorum([("node-a", "A")], expected_nodes=nodes, quorum=2, verifier=lambda _: True)
    with pytest.raises(ProtocolError, match="duplicate voter"):
        decide_quorum([("node-a", "A"), ("node-a", "A")], expected_nodes=nodes, quorum=2, verifier=lambda _: True)
    with pytest.raises(ProtocolError, match="unexpected voter"):
        decide_quorum([("intruder", "A"), ("node-a", "A")], expected_nodes=nodes, quorum=2, verifier=lambda _: True)


def test_idempotency_guard_accepts_operation_once():
    guard = IdempotencyGuard()
    assert guard.accept_once("op-123")
    assert not guard.accept_once("op-123")
    with pytest.raises(ProtocolError, match="required"):
        guard.accept_once("")
