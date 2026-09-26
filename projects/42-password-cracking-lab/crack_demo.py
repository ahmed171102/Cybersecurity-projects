"""Hash a few lab passwords, then dictionary-match those hashes. No other hashes."""

from __future__ import annotations

import hashlib

LAB_PASSWORDS = ("labpass", "summer", "correct-horse")
DICTIONARY = ("labpass", "summer", "winter", "admin")


def md5(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def main() -> None:
    hashes = {name: md5(name) for name in LAB_PASSWORDS}
    print("These hashes were created in this process. Nothing else is cracked.\n")
    for name, digest in hashes.items():
        print(f"stored {digest}  (lab password length {len(name)})")
    print("\nDictionary match against the hashes we just made:")
    recovered = 0
    for digest in hashes.values():
        for guess in DICTIONARY:
            if md5(guess) == digest:
                print(f"matched a lab hash with dictionary word length {len(guess)}")
                recovered += 1
                break
        else:
            print("no dictionary match for one lab hash")
    print(f"\n{recovered} of {len(hashes)} lab hashes matched the small dictionary.")
    print("Lesson: add a salt, use a slow hash, prefer a long passphrase, and turn on MFA.")


if __name__ == "__main__":
    main()
