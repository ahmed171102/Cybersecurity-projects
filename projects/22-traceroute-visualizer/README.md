# 22 — Traceroute visualizer

## What this is

Runs traceroute, tracepath, or Windows tracert against `127.0.0.1`. If the tool is missing, or you pass any other target, it prints a synthetic 4-hop path and writes `path.mmd`.

## Why it matters

A path is a list of routers. When something is "down", the hop where replies stop is the useful fact.

## How to run

```bash
python3 projects/22-traceroute-visualizer/trace.py
```

## Portfolio deliverable

`path.mmd` and one sentence naming your real gateway from `ipconfig` or `ip route`.

## Exercise

Run the script and open path.mmd. Name your real gateway from ipconfig or ip route in one sentence.

