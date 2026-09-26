"""Encrypt or decrypt a file with the shared AES-GCM helper."""

from __future__ import annotations

import argparse
import getpass
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.crypto_utils import decrypt_bytes, encrypt_bytes


def main() -> None:
    parser = argparse.ArgumentParser(description="Encrypt or decrypt one file.")
    parser.add_argument("mode", choices=("encrypt", "decrypt"))
    parser.add_argument("--in", dest="src", required=True)
    parser.add_argument("--out", dest="dst", required=True)
    parser.add_argument("--password")
    args = parser.parse_args()
    password = args.password or getpass.getpass("Password: ")
    data = Path(args.src).read_bytes()
    if args.mode == "encrypt":
        Path(args.dst).write_bytes(encrypt_bytes(data, password))
        print(f"wrote {args.dst}")
    else:
        Path(args.dst).write_bytes(decrypt_bytes(data, password))
        print(f"wrote {args.dst}")


if __name__ == "__main__":
    main()
