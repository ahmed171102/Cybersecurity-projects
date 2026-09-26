# 01 — Network map

## What this is

A JSON inventory of a sample home lab: router, laptop, phone, an IoT bulb, and two virtual machines. Zones are trusted, iot, and lab.

## Why it matters

Every later firewall and VLAN rule needs a picture of who sits where. If the bulb is in the same zone as the laptop, a weak device can reach your files.

## How to run

```bash
python3 projects/01-network-map/map_network.py --sample
```

The command prints a table and writes `diagram.mmd`.

## Portfolio deliverable

A zone diagram you can paste into a README, plus one sentence on why the IoT bulb cannot start a connection to the laptop.

## Exercise

Add a guest phone in the `iot` zone and rerun `--sample`. Confirm the table and `diagram.mmd` both show it.
