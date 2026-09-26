"""Seed two fake users, list them, export one, or delete one."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STORE = ROOT / "privacy_store.json"
EXPORTS = ROOT / "exports"


def load() -> dict:
    if not STORE.exists():
        return {"users": {}}
    return json.loads(STORE.read_text(encoding="utf-8"))


def save(data: dict) -> None:
    STORE.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    data = load()
    if command == "seed":
        data["users"] = {
            "user_1": {"name": "Nora N.", "email": "nora@example.com", "city": "Cairo"},
            "user_2": {"name": "Omar O.", "email": "omar@example.com", "city": "Giza"},
        }
        save(data)
        print("seeded user_1 and user_2")
        return
    if command == "inventory":
        for key, record in data["users"].items():
            print(f"{key} {record['name']} {record['email']}")
        return
    if command == "export" and len(sys.argv) == 3:
        user_id = sys.argv[2]
        if user_id not in data["users"]:
            raise SystemExit("unknown user")
        EXPORTS.mkdir(exist_ok=True)
        path = EXPORTS / f"{user_id}.json"
        path.write_text(json.dumps(data["users"][user_id], indent=2) + "\n", encoding="utf-8")
        print(f"exported {path}")
        return
    if command == "delete" and len(sys.argv) == 3:
        user_id = sys.argv[2]
        if user_id not in data["users"]:
            raise SystemExit("unknown user")
        del data["users"][user_id]
        save(data)
        print(f"deleted {user_id}")
        return
    print("usage: python privacy.py seed | inventory | export user_1 | delete user_1")
    sys.exit(1)


if __name__ == "__main__":
    main()
