# 11 — Backup integrity

## What this is

`create` copies a folder and writes `CHECKSUMS.json`. `verify` hashes every listed file again. `sample_data/` is the folder to practice on.

## Why it matters

A backup you have not checked is a hope. The checksum file is how you notice a silent change.

## How to run

```bash
export PYTHONPATH=$(pwd)
python3 projects/11-backup-integrity/backup.py create projects/11-backup-integrity/sample_data /tmp/lab-backup
python3 projects/11-backup-integrity/backup.py verify /tmp/lab-backup
```

On Windows, use a folder under your user profile instead of `/tmp`.

## Portfolio deliverable

A verify that prints `ok`, then the same command after you edit one copied file, which should exit 1.

## Exercise

Create a backup, verify (ok), edit one copied file, verify again (exit 1). Put the file back and confirm ok.

