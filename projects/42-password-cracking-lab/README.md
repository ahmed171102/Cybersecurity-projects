# 42 — Password cracking lab

## What this is

`crack_demo.py` hashes a few lab passwords with unsalted MD5, dictionary-matches those hashes, and prints the lesson: salt, slow hash, long passphrase, MFA.

## Why it matters

Unsalted MD5 is a teaching example of a bad store. The script only touches hashes it just created.

## How to run

```bash
python3 projects/42-password-cracking-lab/crack_demo.py
```

## Portfolio deliverable

The lesson line, plus one sentence on why project 31 uses Werkzeug instead of MD5.

## Exercise

Add a fourth lab password that is not in the dictionary. Confirm the script says no dictionary match for that hash. Do not add other hashes.

