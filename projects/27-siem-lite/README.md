# 27 — SIEM lite

## What this is

Sample auth, firewall, and web logs. `ingest` writes `events.jsonl`. `alerts` flags 5 or more auth failures, 3 or more firewall denies, and 3 or more web 404 probes. `search TERM` prints matching events.

## Why it matters

A SIEM is a search box with rules. This one is small enough to read in one sitting.

## How to run

```bash
python3 projects/27-siem-lite/siem.py ingest && python3 projects/27-siem-lite/siem.py alerts
python3 projects/27-siem-lite/siem.py search 203.0.113.10
```

## Portfolio deliverable

The three alert lines and a sentence on which source each one came from.

## Exercise

ingest and alerts. Then: python siem.py alerts --auth-threshold 50 and watch the auth alert disappear. Put the threshold away.

