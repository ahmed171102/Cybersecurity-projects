# 09 — Secure notes

## What this is

A command-line vault. `init` creates one encrypted JSON file. `add`, `list`, and `get` decrypt it in memory, then write it back.

## Why it matters

Notes are a normal place for secrets to leak. One encrypted blob is easier to reason about than a folder of plain text files.

## How to run

```bash
export PYTHONPATH=$(pwd)
python3 projects/09-secure-notes/notes.py init --password "lab-password"
python3 projects/09-secure-notes/notes.py add --password "lab-password" --title wifi --body "lab only"
python3 projects/09-secure-notes/notes.py list --password "lab-password"
python3 projects/09-secure-notes/notes.py get --password "lab-password" --title wifi
```

## Portfolio deliverable

Show `vault.enc` in a text editor (it should look random) and the `get` output after the right password.

## Exercise

Init, add two notes, list, get one. Then try the wrong password and confirm the vault does not print the notes.

