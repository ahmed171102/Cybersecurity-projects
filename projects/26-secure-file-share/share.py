"""Encrypt a file and hand out a token that lasts one minute."""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.crypto_utils import decrypt_bytes, encrypt_bytes

ROOT = Path(__file__).resolve().parent
OUTBOX = ROOT / "outbox"
LOG = ROOT / "download.log"


def token_for(name: str, password: str) -> str:
    expires = int(time.time()) + 60
    message = f"{expires}|{name}".encode("utf-8")
    signature = hmac.new(hashlib.sha256(password.encode("utf-8")).digest(), message, hashlib.sha256).hexdigest()
    return base64.urlsafe_b64encode(message + b"|" + signature.encode("ascii")).decode("ascii")


def read_token(token: str, password: str) -> tuple[int, str]:
    raw = base64.urlsafe_b64decode(token.encode("ascii"))
    message, signature = raw.rsplit(b"|", 1)
    expected = hmac.new(hashlib.sha256(password.encode("utf-8")).digest(), message, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature.decode("ascii")):
        raise SystemExit("bad token")
    expires_text, name = message.decode("utf-8").split("|", 1)
    return int(expires_text), name


def main() -> None:
    parser = argparse.ArgumentParser(description="Expiring encrypted file share.")
    parser.add_argument("command", choices=("put", "get"))
    parser.add_argument("--password", required=True)
    parser.add_argument("--file")
    parser.add_argument("--token")
    parser.add_argument("--out")
    args = parser.parse_args()
    OUTBOX.mkdir(exist_ok=True)
    if args.command == "put":
        source = Path(args.file)
        target = OUTBOX / (source.name + ".enc")
        target.write_bytes(encrypt_bytes(source.read_bytes(), args.password))
        print(token_for(source.name, args.password))
        return
    expires, name = read_token(args.token, args.password)
    if time.time() > expires:
        raise SystemExit("token expired")
    blob = (OUTBOX / f"{name}.enc").read_bytes()
    Path(args.out).write_bytes(decrypt_bytes(blob, args.password))
    with LOG.open("a", encoding="utf-8") as handle:
        handle.write(f"{int(time.time())} {name}\n")
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
