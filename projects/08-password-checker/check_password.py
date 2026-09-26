"""Score a password on this machine. Nothing is stored or sent."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

COMMON = {
    line.strip().lower()
    for line in (Path(__file__).resolve().parent / "common.txt").read_text(encoding="utf-8").splitlines()
    if line.strip()
}


def entropy(password: str) -> float:
    pool = 0
    if any(char.islower() for char in password):
        pool += 26
    if any(char.isupper() for char in password):
        pool += 26
    if any(char.isdigit() for char in password):
        pool += 10
    if any(not char.isalnum() for char in password):
        pool += 32
    if pool == 0 or not password:
        return 0.0
    return round(len(password) * math.log2(pool), 1)


def score(password: str) -> int:
    if password.lower() in COMMON:
        return 0
    points = 0
    points += len(password) >= 8
    points += len(password) >= 12
    points += any(char.islower() for char in password) and any(char.isupper() for char in password)
    points += any(char.isdigit() for char in password)
    points += any(not char.isalnum() for char in password)
    return points


def main() -> None:
    parser = argparse.ArgumentParser(description="Local password score. The value is not saved.")
    parser.add_argument("--password", required=True)
    args = parser.parse_args()
    value = args.password
    print(f"score {score(value)}/5")
    print(f"rough entropy {entropy(value)} bits")
    print("not stored, not sent")
    if value.lower() in COMMON:
        print("this is on the small common-password list")


if __name__ == "__main__":
    main()
