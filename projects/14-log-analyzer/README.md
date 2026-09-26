# 14 — Log analyzer

## What this is

Reads lines shaped like `TIMESTAMP OK|FAIL user= ip=`. An IP with 5 or more failures is an alert. The sample log alerts on `203.0.113.10`.

## Why it matters

One wrong password is normal. The same address failing over and over is the pattern worth a human look.

## How to run

```bash
python3 projects/14-log-analyzer/analyze.py projects/14-log-analyzer/sample_auth.log
```

## Portfolio deliverable

The alert line, and a second run after you add one more failure from a different address that should stay quiet.

## Exercise

Raise the bar until the sample goes quiet:

```bash
python3 projects/14-log-analyzer/analyze.py projects/14-log-analyzer/sample_auth.log --threshold 20
```

That is a false negative. Put the threshold back to 5.
