"""Password-based encryption for the learning labs.

On disk the blob is: salt (16 bytes) | nonce (12 bytes) | ciphertext and tag.
The key is PBKDF2-HMAC-SHA256, 200_000 iterations, 32 bytes.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ITERATIONS = 200_000


def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS,
        dklen=32,
    )


def encrypt_bytes(data: bytes, password: str) -> bytes:
    salt = os.urandom(16)
    nonce = os.urandom(12)
    ciphertext = AESGCM(derive_key(password, salt)).encrypt(nonce, data, None)
    return salt + nonce + ciphertext


def decrypt_bytes(blob: bytes, password: str) -> bytes:
    if len(blob) < 16 + 12 + 16:
        raise ValueError("file is too short to be an encrypted blob")
    salt, nonce, ciphertext = blob[:16], blob[16:28], blob[28:]
    return AESGCM(derive_key(password, salt)).decrypt(nonce, ciphertext, None)


def encrypt_text(text: str, password: str) -> bytes:
    return encrypt_bytes(text.encode("utf-8"), password)


def decrypt_text(blob: bytes, password: str) -> str:
    return decrypt_bytes(blob, password).decode("utf-8")


def sha256_file(path: Path | str) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()
