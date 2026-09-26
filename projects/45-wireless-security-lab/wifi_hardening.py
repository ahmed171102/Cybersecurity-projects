"""Print wireless hardening steps for an access point you own."""

from __future__ import annotations

STEPS = [
    "Use WPA3 if the phones and laptops support it. If not, WPA2-AES. Do not leave WPA or TKIP on.",
    "Set a long passphrase. A short Wi-Fi password is shared with every guest forever.",
    "Disable WPS. The PIN on the box is a short secret sitting in plain sight.",
    "Put IoT devices on a separate SSID and VLAN (see project 19). They should not start connections to the laptops.",
    "Update access-point firmware. Old firmware is a known hole with a download link.",
    "Turn off administration from the WAN. Manage the AP from the trusted LAN only.",
]


def main() -> None:
    print("Hardening for a wireless network you own. Do not test a neighbor's AP.\n")
    for index, step in enumerate(STEPS, start=1):
        print(f"{index}. {step}")


if __name__ == "__main__":
    main()
