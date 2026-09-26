# 44 — Active Directory lab

## What this is

`ad_concepts.py` prints Kerberoasting, AS-REP roasting, pass-the-hash, DCSync, and golden ticket. Each line has one defense. There are no attack scripts.

## Why it matters

Directory attacks are named in every junior job post. The skill that travels is the defense sentence, not a tool command.

## How to run

```bash
python3 projects/44-active-directory-lab/ad_concepts.py
```

## Portfolio deliverable

Five defense lines in your own words, plus which one you would check first on a lab domain controller.

## Exercise

Add a sixth row for "unconstrained delegation" and one defense (do not allow a workstation to impersonate anyone to any service). Keep the print loop unchanged.
