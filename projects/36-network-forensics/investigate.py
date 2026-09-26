"""Print a synthetic case timeline. No live capture."""

from __future__ import annotations

EVENTS = [
    "2026-09-26T01:00:00Z  DNS query updates.example.invalid from 10.0.0.40",
    "2026-09-26T01:00:01Z  DNS answer 203.0.113.77",
    "2026-09-26T01:00:02Z  TLS handshake to 203.0.113.77:443",
    "2026-09-26T01:05:00Z  periodic connection every 60s to the same host",
    "2026-09-26T02:10:00Z  12MB upload from 10.0.0.40 to 203.0.113.77",
]


def main() -> None:
    print("Synthetic investigation. Do not contact 203.0.113.77.")
    for line in EVENTS:
        print(line)
    print("Question for the report: is this an approved updater, or a new destination plus a large outbound transfer?")


if __name__ == "__main__":
    main()
