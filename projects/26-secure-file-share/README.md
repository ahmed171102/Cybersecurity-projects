# 26 — Secure file share

## What this is

`put` encrypts a file and prints a token that expires in one minute. `get` decrypts it when the token is still valid and appends a line to `download.log`.

## Why it matters

A link that lives forever is a file you no longer control. Expiry plus a log is the smallest share you can explain.

## How to run

```bash
export PYTHONPATH=$(pwd)
python3 projects/26-secure-file-share/share.py put --password "lab-password" --file README.md
python3 projects/26-secure-file-share/share.py get --password "lab-password" --token PASTE --out copy.md
```

Use the token within a minute.

## Portfolio deliverable

A successful get, then the same token after you wait, which should say it expired.

## Exercise

put a small file, get it within a minute, then wait and reuse the token. The second get should say expired.

