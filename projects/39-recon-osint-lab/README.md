# 39 — Recon and OSINT lab

## What this is

`--domain example.com --passive` does DNS only. `--target --local-services` probes a few ports and refuses non-lab hosts unless `--i-have-authorization` is passed. That flag appends a line to `engagement_log.txt`.

## Why it matters

Recon is reading names. A port check is already a test. The log is how you prove you had a reason.

## How to run

```bash
python3 projects/39-recon-osint-lab/recon.py --domain example.com --passive
python3 projects/39-recon-osint-lab/recon.py --target 127.0.0.1 --local-services
```

## Portfolio deliverable

The passive DNS output and one engagement-log line from a host that was in a written lab scope.

## Exercise

Passive DNS for example.com. Then --target 8.8.8.8 --local-services and confirm it refuses without --i-have-authorization.

