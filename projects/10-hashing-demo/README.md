# 10 — Hashing demo

## What this is

`hash` prints the SHA-256 of a file. `verify` exits 1 when the digest does not match.

## Why it matters

A hash is a fingerprint, not a lock. You publish the fingerprint so someone else can see whether the file changed. You cannot turn the hash back into the file.

## How to run

```bash
export PYTHONPATH=$(pwd)
python3 projects/10-hashing-demo/hash_demo.py hash README.md
python3 projects/10-hashing-demo/hash_demo.py verify README.md PASTE_THE_DIGEST
```

## Portfolio deliverable

The digest before and after you change one character in a copy of the file.

## Exercise

Hash a file, change one character, hash again. The digest must change. verify on the old digest should exit 1.

