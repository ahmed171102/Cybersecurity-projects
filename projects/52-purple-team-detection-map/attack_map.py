"""Map five behaviors to a detection and a mitigation."""

from __future__ import annotations

import argparse

ROWS = [
    (
        "port scan",
        "Many closed ports from one source in a short window (project 27 firewall denies).",
        "Allow only the ports you need. Alert on a source that hits many ports (project 06 stays on lab hosts).",
    ),
    (
        "phishing",
        "Users report lookalike mail. Gateway sees the same link to several people (project 15).",
        "Open the official app. Quarantine copies. Do not use the link.",
    ),
    (
        "password guessing",
        "Five or more FAIL lines from one IP (projects 14 and 27).",
        "Lockout, MFA, and reset the password if a success follows the failures.",
    ),
    (
        "hash reuse",
        "The same password hash works on a second host (project 44 pass-the-hash).",
        "Unique local admin passwords. Credential Guard on Windows labs.",
    ),
    (
        "large outbound transfer",
        "A 12MB upload after a new DNS name (project 36).",
        "Ask the owner of the host. Block the destination if it is not an approved updater.",
    ),
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Detection map.")
    parser.add_argument("--tactic", action="store_true", help="Print the five rows.")
    args = parser.parse_args()
    if not args.tactic:
        print("usage: python attack_map.py --tactic")
        raise SystemExit(1)
    print("Purple-team map. Offense names on the left, defense on the right.\n")
    for name, detection, mitigation in ROWS:
        print(name)
        print(f"  detect: {detection}")
        print(f"  mitigate: {mitigation}")
        print()


if __name__ == "__main__":
    main()
