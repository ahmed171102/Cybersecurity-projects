# 45 — Wireless security lab

## What this is

`wifi_hardening.py` prints WPA3 or WPA2-AES, a long passphrase, disable WPS, a separate IoT SSID, firmware updates, and no WAN admin. Own access point only.

## Why it matters

Most home breaches start with a shared password or a guest device on the same network as the laptop.

## How to run

```bash
python3 projects/45-wireless-security-lab/wifi_hardening.py
```

## Portfolio deliverable

A photo of your own AP settings with the SSID blurred, showing WPA2-AES or WPA3 and WPS off.

## Exercise

Write one extra step: guest network isolated from LAN. Add it to the list and rerun.
