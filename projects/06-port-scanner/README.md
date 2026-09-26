# 06 — Port scanner

## What this is

A TCP connect scanner. The default host is `127.0.0.1`. If you omit ports, it checks a short list of common ones. Anything that is not loopback or a private address is refused.

## Why it matters

A port scan is an inventory of doors. It is also easy to point at the wrong building. This copy will not open that door for you.

## How to run

```bash
python3 projects/06-port-scanner/scanner.py 127.0.0.1 --ports 1-20
python3 projects/06-port-scanner/scanner.py 8.8.8.8 --ports 80
```

The second command should refuse the target and exit 2.

## Portfolio deliverable

Output from your own machine, plus the refusal line for a public address, and a sentence on what "open" means.

## Exercise

Scan 127.0.0.1 ports 1-20, then 8.8.8.8. The second command must refuse. Add one common port to the default list and scan again.

