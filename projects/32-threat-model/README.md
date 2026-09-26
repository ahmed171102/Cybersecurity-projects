# 32 — Threat model

## What this is

A STRIDE table and a data-flow diagram for the notes app in project 31. `stride_helper.py` prints the six letters.

## Why it matters

A threat model is how you choose the next control. It is also how you explain the app in an interview without reading the code line by line.

## How to run

```bash
python3 projects/32-threat-model/stride_helper.py
```

## Portfolio deliverable

The table in `STRIDE.md` with one extra row you wrote for a threat the current code does not cover yet. This is a CV project. See `docs/CV_AND_PORTFOLIO.md`.

## Resume line

Wrote a STRIDE model for that notes app and tied each threat to a control already in the code.

## Exercise

```bash
python3 projects/32-threat-model/stride_helper.py --letter I
```

Only the information-disclosure line should print. Then add a length limit note to the D row if you have not already.
