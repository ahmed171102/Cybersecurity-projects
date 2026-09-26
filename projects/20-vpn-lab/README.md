# 20 — VPN lab

## What this is

A WireGuard sample config. The key fields say `REPLACE_WITH_PRIVATE_KEY` and `REPLACE_WITH_SERVER_PUBLIC_KEY`. There is no real private key in this repo. `WRITEUP_TEMPLATE.md` is the note you fill after you build a lab tunnel.

## Why it matters

A VPN is a chosen path for packets, not a magic shield. `AllowedIPs` is the list of destinations that use the tunnel. A private key in git is a lost laptop.

## How to run

Read `wg0.conf.sample`. Generate keys on the lab VM with WireGuard's own tools, and keep them out of this repository.

## Portfolio deliverable

A write-up that shows the tunnel address and the AllowedIPs line, with the private key redacted.

## Exercise

Fill WRITEUP_TEMPLATE.md with AllowedIPs = 10.8.0.0/24. Generate keys on the VM only. Never paste a private key into git.

