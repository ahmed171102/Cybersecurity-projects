# 28 — IDS lab

## What this is

`ids_sim.py` alerts on TCP/23 and TCP/445 and passes TCP/443. The events are sample data. There is no live attack traffic. `RULES.md` and `WRITEUP.md` are the notes around it.

## Why it matters

An IDS watches a copy of traffic and raises a hand. Port 443 by itself is not an incident. Port 23 on a modern lab usually is.

## How to run

```bash
python3 projects/28-ids-lab/ids_sim.py
```

## Portfolio deliverable

The three output lines and a filled write-up that names one expected false positive.

## Exercise

Add a sample event for TCP/3389 and an alert reason. Confirm 443 still prints pass.

