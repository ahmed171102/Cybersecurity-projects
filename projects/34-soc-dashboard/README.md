# 34 — SOC dashboard

## What this is

`build_sample_alerts.py` writes four sample alerts. Flask on `127.0.0.1:5003` shows counts and a status dropdown that saves open, triaging, or closed.

## Why it matters

A SOC queue is a list with a status. The work is deciding, then writing the new status down.

## How to run

```bash
python3 projects/34-soc-dashboard/build_sample_alerts.py
python3 projects/34-soc-dashboard/app.py
```

Open http://127.0.0.1:5003/ and move the HIGH brute-force alert from open to triaging.

## Portfolio deliverable

A screenshot of the counts after you change one status.

## Exercise

Build alerts, open the board, move the HIGH item to triaging, refresh, and confirm the counts changed.

