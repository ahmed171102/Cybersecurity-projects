"""A tiny role check: admin, analyst, guest."""

from __future__ import annotations

import argparse
import sys

USERS = {"alice": "admin", "bob": "analyst", "carol": "guest"}
PERMISSIONS = {
    "admin": {"read_reports", "write_reports", "delete_users"},
    "analyst": {"read_reports", "write_reports"},
    "guest": {"read_reports"},
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Allow or deny one action.")
    parser.add_argument("--user", required=True)
    parser.add_argument("--action", required=True)
    parser.add_argument("--explain", action="store_true")
    args = parser.parse_args()
    if args.explain:
        print("roles: " + ", ".join(f"{name}={role}" for name, role in USERS.items()))
        for role, actions in PERMISSIONS.items():
            print(f"{role} may {', '.join(sorted(actions))}")
    role = USERS.get(args.user)
    if role is None:
        print("DENY unknown user")
        sys.exit(1)
    if args.action in PERMISSIONS[role]:
        print(f"ALLOW {args.user} ({role}) {args.action}")
        return
    print(f"DENY {args.user} ({role}) {args.action}")
    sys.exit(1)


if __name__ == "__main__":
    main()
