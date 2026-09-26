"""Fail if another Python file in this folder hard-codes a secret assignment."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PATTERN = re.compile(
    r"^\s*(SECRET|PASSWORD|API_KEY|TOKEN)\s*=\s*['\"][^'\"]+['\"]",
    re.IGNORECASE,
)


def main() -> None:
    hits = []
    for path in ROOT.glob("*.py"):
        if path.name == "security_gate.py":
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if PATTERN.search(line):
                hits.append(f"{path.name}:{number}: {line.strip()}")
    if hits:
        print("hard-coded secret assignment found")
        for hit in hits:
            print(hit)
        sys.exit(1)
    print("no hard-coded secret assignment")


if __name__ == "__main__":
    main()
