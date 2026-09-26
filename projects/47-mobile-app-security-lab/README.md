# 47 — Mobile app security lab

## What this is

A checklist: hard-coded keys, plaintext storage, missing TLS, extra permissions, debug flags, and noisy logs.

## Why it matters

A mobile client is another place secrets sit. Reviewers look at storage and TLS before they look at the pretty screens.

## How to run

```bash
python3 projects/47-mobile-app-security-lab/mobile_checklist.py
```

## Portfolio deliverable

The six lines applied to an app you wrote or a teaching app, with pass/fail next to each.

## Exercise

Add a seventh item: backup exclusion for the local database so a stolen laptop backup does not include session tokens.
