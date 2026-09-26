# 36 — Network forensics

## What this is

`investigate.py` prints a synthetic timeline: DNS to `updates.example.invalid`, answer `203.0.113.77`, TLS, periodic connections, then a 12MB upload. `CASE_REPORT.md` is the write-up.

## Why it matters

A name, an address, a timer, and a large upload is the story you write before you call it data leaving the lab.

## How to run

```bash
python3 projects/36-network-forensics/investigate.py
```

## Portfolio deliverable

A filled case report that names the 12MB upload as the fact that needs an owner, not as proof of malware.

## Exercise

Fill CASE_REPORT.md. The 12MB upload is a question for the owner, not a malware verdict.

