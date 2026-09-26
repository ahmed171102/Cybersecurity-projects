# 21 — Network monitor

## What this is

Pings a target a few times, writes `metrics.csv`, and prints an alert if a reply is missing or slower than the threshold. The default target is `127.0.0.1`. Public addresses are refused.

## Why it matters

Availability is the "A" in CIA. A missing reply is a fact you can put on a timeline.

## How to run

```bash
python3 projects/21-network-monitor/monitor.py --target 127.0.0.1 --count 3 --threshold 100
```

## Portfolio deliverable

The CSV from your own machine and one sentence on what you would page a person for.

## Exercise

Ping 127.0.0.1 three times. Then set --threshold 0 and confirm you get alerts on normal latency. Put the threshold back.

