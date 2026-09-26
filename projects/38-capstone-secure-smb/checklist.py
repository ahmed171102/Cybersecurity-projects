"""Print the eight-item capstone checklist."""

from __future__ import annotations

ITEMS = [
    "map — project 01: who sits in trusted, IoT, and lab",
    "firewall — project 17: default deny, LAN SSH only",
    "hardening — project 18: read-only host check",
    "secure app — project 31: hash, CSRF, parameters",
    "backup — project 11: checksums you can verify",
    "SIEM — project 27: ingest and alerts",
    "IR — project 29: contain before you wipe",
    "policies — project 37: classify, access, recover",
]


def main() -> None:
    print("Capstone checklist for a small company")
    for index, item in enumerate(ITEMS, start=1):
        print(f"{index}. {item}")


if __name__ == "__main__":
    main()
