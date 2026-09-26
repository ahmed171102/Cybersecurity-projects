# 51 — CTF practice tracker

## What this is

`ctf_tracker.py add NAME CATEGORY easy|medium|hard`, `list`, and `stats`. Progress lives in `progress.json`. A seed list is used until you add your own.

## Why it matters

Practice without a list repeats the same easy room. The tracker is how you see what you have not touched.

## How to run

```bash
python3 projects/51-ctf-practice-tracker/ctf_tracker.py list
python3 projects/51-ctf-practice-tracker/ctf_tracker.py add "Bandit 1" linux easy
python3 projects/51-ctf-practice-tracker/ctf_tracker.py stats
```

## Portfolio deliverable

A stats line after ten rooms on TryHackMe or OverTheWire, written in your own notes.

## Exercise

Add a `search TERM` command that prints matching names. Keep `list` printing the word `challenge`.
