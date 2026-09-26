# 24 — Secrets manager

## What this is

`init`, `set`, `get`, `rotate`, `list`, and `audit`. Values live in one encrypted file. Names and actions are appended to `audit.log`. `list` prints names, not values.

## Why it matters

A secret in a source file gets copied forever. A store with an audit line answers "who read this" later.

## How to run

```bash
export PYTHONPATH=$(pwd)
python3 projects/24-secrets-manager/secrets.py init --password "lab-password"
python3 projects/24-secrets-manager/secrets.py set --password "lab-password" --name db --value "lab-only"
python3 projects/24-secrets-manager/secrets.py rotate --password "lab-password" --name db --value "lab-only-2"
python3 projects/24-secrets-manager/secrets.py audit --password "lab-password"
```

## Portfolio deliverable

The audit log after a set and a rotate, with the values redacted in the screenshot.

## Exercise

Set, get, rotate, list, audit. Confirm list prints names only. Confirm audit.log has set and rotate lines.

