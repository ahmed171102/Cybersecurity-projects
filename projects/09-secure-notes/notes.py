"""One encrypted JSON blob used as a note vault."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.crypto_utils import decrypt_text, encrypt_text

VAULT = Path(__file__).resolve().parent / "vault.enc"


def load(password: str) -> list[dict]:
    if not VAULT.exists():
        raise SystemExit("run init first")
    return json.loads(decrypt_text(VAULT.read_bytes(), password))


def save(notes: list[dict], password: str) -> None:
    VAULT.write_bytes(encrypt_text(json.dumps(notes), password))


def main() -> None:
    parser = argparse.ArgumentParser(description="Encrypted note vault.")
    parser.add_argument("command", choices=("init", "add", "list", "get"))
    parser.add_argument("--password", required=True)
    parser.add_argument("--title")
    parser.add_argument("--body")
    args = parser.parse_args()
    if args.command == "init":
        if VAULT.exists():
            raise SystemExit("vault already exists")
        save([], args.password)
        print("initialized empty vault")
        return
    notes = load(args.password)
    if args.command == "add":
        if not args.title or not args.body:
            raise SystemExit("add needs --title and --body")
        notes.append({"title": args.title, "body": args.body})
        save(notes, args.password)
        print(f"saved {args.title}")
    elif args.command == "list":
        for note in notes:
            print(note["title"])
        if not notes:
            print("(empty)")
    else:
        for note in notes:
            if note["title"] == args.title:
                print(note["body"])
                return
        raise SystemExit("no note with that title")


if __name__ == "__main__":
    main()
