"""SHA-256 a file, or check a digest you already have."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.crypto_utils import sha256_file


def main() -> None:
    if len(sys.argv) < 3 or sys.argv[1] not in {"hash", "verify"}:
        print("usage: python hash_demo.py hash FILE")
        print("       python hash_demo.py verify FILE DIGEST")
        sys.exit(1)
    digest = sha256_file(sys.argv[2])
    if sys.argv[1] == "hash":
        print(digest)
        return
    if len(sys.argv) != 4:
        print("verify needs a digest")
        sys.exit(1)
    if digest.lower() == sys.argv[3].lower():
        print("match")
        return
    print("mismatch")
    sys.exit(1)


if __name__ == "__main__":
    main()
