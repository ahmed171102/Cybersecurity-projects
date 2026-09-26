"""Encrypted secret store with an append-only audit log."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.crypto_utils import decrypt_text, encrypt_text

ROOT = Path(__file__).resolve().parent
STORE = ROOT / "secrets.enc"
AUDIT = ROOT / "audit.log"


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def audit(action: str, name: str) -> None:
    with AUDIT.open("a", encoding="utf-8") as handle:
        handle.write(f"{now()} {action} {name}\n")


def load(password: str) -> dict:
    if not STORE.exists():
        raise SystemExit("run init first")
    return json.loads(decrypt_text(STORE.read_bytes(), password))


def save(data: dict, password: str) -> None:
    STORE.write_bytes(encrypt_text(json.dumps(data), password))


def main() -> None:
    parser = argparse.ArgumentParser(description="Lab secret store.")
    parser.add_argument("command", choices=("init", "set", "get", "rotate", "list", "audit"))
    parser.add_argument("--password", required=True)
    parser.add_argument("--name")
    parser.add_argument("--value")
    args = parser.parse_args()
    if args.command == "init":
        if STORE.exists():
            raise SystemExit("store already exists")
        save({}, args.password)
        audit("init", "-")
        print("initialized")
        return
    if args.command == "audit":
        print(AUDIT.read_text(encoding="utf-8") if AUDIT.exists() else "(empty)")
        return
    data = load(args.password)
    if args.command == "list":
        for name in sorted(data):
            print(name)
        audit("list", "-")
        return
    if not args.name:
        raise SystemExit("this command needs --name")
    if args.command == "get":
        if args.name not in data:
            raise SystemExit("missing")
        print(data[args.name])
        audit("get", args.name)
        return
    if not args.value:
        raise SystemExit("set and rotate need --value")
    data[args.name] = args.value
    save(data, args.password)
    audit(args.command, args.name)
    print(f"{args.command} {args.name}")


if __name__ == "__main__":
    main()
