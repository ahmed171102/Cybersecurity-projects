# 17 — Firewall lab

## What this is

A UFW cheat sheet and a first-match simulator. LAN SSH is allowed, public SSH is denied, public port 80 is allowed, and 3389 is denied.

## Why it matters

Rules are read from the top. A later deny does nothing if an earlier allow already matched. Default deny incoming is the starting point.

## How to run

```bash
python3 projects/17-firewall-lab/policy_sim.py
```

Apply the UFW commands only on a lab VM.

## Portfolio deliverable

The four simulator lines, and a sentence on which rule matches public SSH.

## Exercise

Read the four public/LAN lines. Then explain why 192.168.1.20:443 is denied. Add an ALLOW 443 LAN rule at the top and rerun.

