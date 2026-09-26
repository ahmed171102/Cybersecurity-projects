# 07 — File encryptor

## What this is

Encrypts and decrypts one file. The format is salt, nonce, then ciphertext, using `shared.crypto_utils`.

## Why it matters

A password should not be the file's encryption key by itself. PBKDF2 stretches the password. AES-GCM then hides the bytes and notices if they were edited.

## How to run

```bash
export PYTHONPATH=$(pwd)
python3 projects/07-file-encryptor/encryptor.py encrypt --password "lab-password" --in notes.txt --out notes.enc
python3 projects/07-file-encryptor/encryptor.py decrypt --password "lab-password" --in notes.enc --out notes.out
```

Leave off `--password` if you want a hidden prompt.

## Portfolio deliverable

Show the encrypted file is unreadable, then show the decrypted file matches the original. Mention the 200,000 PBKDF2 iterations.

## Exercise

Encrypt a file, change one byte of the .enc file in a hex editor or by appending a character, and confirm decrypt fails. That is the GCM tag doing its job.

