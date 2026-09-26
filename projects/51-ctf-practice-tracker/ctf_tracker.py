"""Record practice challenges. Legal platforms only."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

STORE = Path(__file__).resolve().parent / "progress.json"
SEED = [
    {"name": "Bandit 0", "category": "linux", "level": "easy"},
    {"name": "PortSwigger SQLi 1", "category": "web", "level": "easy"},
]


def load() -> list[dict]:
    if STORE.exists():
        return json.loads(STORE.read_text(encoding="utf-8"))
    return list(SEED)


def save(rows: list[dict]) -> None:
    STORE.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Track CTF practice.")
    parser.add_argument("command", choices=("add", "list", "stats"))
    parser.add_argument("name", nargs="?")
    parser.add_argument("category", nargs="?")
    parser.add_argument("level", nargs="?", choices=("easy", "medium", "hard"))
    args = parser.parse_args()
    rows = load()
    if args.command == "add":
        if not (args.name and args.category and args.level):
            raise SystemExit("add needs NAME CATEGORY easy|medium|hard")
        rows.append({"name": args.name, "category": args.category, "level": args.level})
        save(rows)
        print(f"added {args.name}")
        return
    if args.command == "list":
        print("challenge list")
        for row in rows:
            print(f"{row['level']:<7} {row['category']:<10} {row['name']}")
        return
    counts = Counter(row["level"] for row in rows)
    print(f"total {len(rows)}  easy {counts.get('easy', 0)}  medium {counts.get('medium', 0)}  hard {counts.get('hard', 0)}")


if __name__ == "__main__":
    main()
