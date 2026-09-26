# 02 — Packet capture lab

## What this is

A cheatsheet, a worksheet, a sample DNS and TCP write-up, and a script that prints a 7-packet story: ping, DNS for example.com, then a TCP handshake to port 443.

## Why it matters

Alerts and firewall rules are easier once you can see the order of packets. Ping, DNS, and the handshake are the three patterns that show up everywhere.

## How to run

```bash
python3 projects/02-packet-capture-lab/generate_synthetic_pcap_notes.py
```

Then read `CHEATSHEET.md` before you open Wireshark on a lab VM. Only capture networks you own.

## Portfolio deliverable

The worksheet filled in from a 10-packet capture on your own VM, with the three handshake packets named.

## Exercise

Circle packets 5-7 on the printed story and write SYN, SYN-ACK, ACK next to them. Then capture 10 packets on a VM you own and fill WORKSHEET.md.

