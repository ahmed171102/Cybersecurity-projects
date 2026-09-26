"""Lint an IAM policy JSON. Own accounts only."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def findings_for(policy: dict) -> list[str]:
    notes = []
    for statement in policy.get("Statement", []):
        sid = statement.get("Sid", "unnamed")
        action = statement.get("Action")
        resource = statement.get("Resource")
        if action == "*" or action == ["*"]:
            notes.append(f"{sid}: Action * lets this principal do every API call")
        if resource == "*" or resource == ["*"]:
            notes.append(f"{sid}: Resource * applies to every object in the account")
        actions = action if isinstance(action, list) else [action]
        if "iam:PassRole" in actions and (resource == "*" or resource == ["*"]):
            notes.append(f"{sid}: iam:PassRole on * can hand a powerful role to a service")
    return notes


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: python iam_lint.py sample_policy.json")
        sys.exit(2)
    policy = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    notes = findings_for(policy)
    print("IAM findings")
    if not notes:
        print("none")
        return
    for note in notes:
        print(f"- {note}")
    sys.exit(1)


if __name__ == "__main__":
    main()
