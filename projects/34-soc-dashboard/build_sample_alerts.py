"""Write the four sample alerts the dashboard reads."""

from __future__ import annotations

import json
from pathlib import Path

ALERTS = [
    {"id": "1", "title": "Brute force", "severity": "HIGH", "status": "open"},
    {"id": "2", "title": "Firewall denies", "severity": "MED", "status": "triaging"},
    {"id": "3", "title": "Web probe", "severity": "MED", "status": "closed"},
    {"id": "4", "title": "Login noise", "severity": "LOW", "status": "closed"},
]


def main() -> None:
    path = Path(__file__).resolve().parent / "alerts.json"
    path.write_text(json.dumps(ALERTS, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {path.name}")


if __name__ == "__main__":
    main()
