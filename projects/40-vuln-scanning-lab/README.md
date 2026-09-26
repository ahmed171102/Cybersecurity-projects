# 40 — Vulnerability scanning lab

## What this is

Sample findings in JSON. `triage.py` ranks them by CVSS, plus 2 if an exploit exists, times 1.0 / 1.3 / 1.6 for low / medium / high asset value. Bands are P1–P4.

## Why it matters

A scanner dump is a list. Priority is the list after someone decided what the asset is worth.

## How to run

```bash
python3 projects/40-vuln-scanning-lab/triage.py
```

Run scanners only on lab VMs you own.

## Portfolio deliverable

The ranked list and one sentence on why a medium CVSS on a high-value host can beat a higher score on a printer.

## Exercise

Lower V-1 asset_value to low and rerun. Watch it drop below the IDOR finding. Put high back.

