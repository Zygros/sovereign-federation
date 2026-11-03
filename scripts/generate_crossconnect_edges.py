#!/usr/bin/env python3
"""Generate the directed logical federation graph from the canonical index."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "FEDERATION_INDEX.json"
CROSSCONNECT = ROOT / ".phoenix" / "CROSSCONNECT.json"
OUT = ROOT / "graph" / "repository_edges.jsonl"


def load_repositories():
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    entries = index.get("repos")
    if not isinstance(entries, list) or not entries:
        raise ValueError("FEDERATION_INDEX.json must contain a non-empty repos array")
    names = []
    for entry in entries:
        name = entry.get("name") if isinstance(entry, dict) else None
        if not isinstance(name, str) or not name.strip():
            raise ValueError("every federation index entry must have a non-empty name")
        names.append(name)
    if len(names) != len(set(names)):
        raise ValueError("FEDERATION_INDEX.json contains duplicate repository names")
    crossconnect = json.loads(CROSSCONNECT.read_text(encoding="utf-8"))
    if crossconnect.get("schema") != "phoenix-crossconnect/v1":
        raise ValueError("unsupported federation crossconnect schema")
    if crossconnect.get("repositories") != names:
        raise ValueError("CROSSCONNECT repositories must exactly match FEDERATION_INDEX.json order")
    return names


def main():
    repositories = load_repositories()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with OUT.open("w", encoding="utf-8", newline="\n") as handle:
        for source in repositories:
            for target in repositories:
                if source == target:
                    continue
                handle.write(json.dumps({
                    "source": source,
                    "target": target,
                    "edge": "logical-federation",
                    "actions": "shared-action-contract",
                }, sort_keys=True) + "\n")
                count += 1
    expected = len(repositories) * (len(repositories) - 1)
    if count != expected:
        raise AssertionError((count, expected))
    print(f"nodes={len(repositories)} generated={count} expected={expected}")


if __name__ == "__main__":
    main()
