"""Print five timestamped events from a finished lab incident."""

from __future__ import annotations

EVENTS = [
    ("2026-09-26T02:14:00Z", "46 failed logons, then a success, on FIN-PC-04"),
    ("2026-09-26T02:20:00Z", "analyst isolates the PC from the lab network"),
    ("2026-09-26T03:22:00Z", "new admin account support-temp appears on the directory"),
    ("2026-09-26T03:40:00Z", "security log cleared on FIN-PC-04"),
    ("2026-09-26T05:00:00Z", "both accounts disabled and the exposed password reset"),
]


def main() -> None:
    print("timeline")
    for when, what in EVENTS:
        print(f"{when}  {what}")


if __name__ == "__main__":
    main()
