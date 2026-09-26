# 19 — VLAN home lab

## What this is

A Mermaid diagram and a written policy. VLAN 10 is trusted (`192.168.10.0/24`). VLAN 20 is IoT. VLAN 30 is the lab. The default between them is deny. IoT cannot start connections to trusted.

## Why it matters

A flat home network means one weak bulb is on the same network as your laptop. VLANs are how you draw the walls.

## How to run

Open `vlan.mmd` in a Mermaid preview, and read `POLICY.md`. No install is required.

## Portfolio deliverable

The diagram plus one allow rule you would add, with the source, destination, and port written down.

## Exercise

Write one extra allow: trusted may reach lab TCP/22 for administration. Keep IoT unable to start connections to trusted.

