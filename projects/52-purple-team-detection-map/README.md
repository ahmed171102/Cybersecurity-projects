# 52 — Purple team detection map

## What this is

`attack_map.py --tactic` prints five rows: port scan, phishing, password guessing, hash reuse, and a large outbound transfer. Each row has a detection and a mitigation.

## Why it matters

Purple team is the sentence that joins a behavior you can name with a log you can search.

## How to run

```bash
python3 projects/52-purple-team-detection-map/attack_map.py --tactic
```

## Portfolio deliverable

A sixth row you add for "new local admin" using events 4720 and 4732 from the earlier labs.

## Exercise

Add `--only password` that prints one row. Keep `--tactic` printing all five including the word `phishing`.
