# 05 — Subnet calculator

## What this is

Given an IP and a prefix, print the network, broadcast, mask, wildcard, and usable hosts. `--binary` shows the address and the mask as bits.

## Why it matters

Firewall rules and VLANs are ranges, not single computers. `/24` is the range you will see most often in a home lab.

## How to run

```bash
python3 projects/05-subnet-calculator/subnet.py 192.168.1.10/24 --binary
```

## Portfolio deliverable

A screenshot of `/24` and `/26` for the same address, with one sentence on why `/26` has fewer hosts.

## Exercise

Run the same address as /24 and /26. Write why /26 has fewer hosts. Then try your own IP from ipconfig with its prefix.

