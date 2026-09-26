"""Ingest three sample logs, raise alerts, or search the events."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EVENTS = ROOT / "events.jsonl"


def parse_auth(line: str) -> dict | None:
    parts = line.split()
    if len(parts) < 4:
        return None
    return {
        "time": parts[0],
        "source": "auth",
        "action": parts[1],
        "user": parts[2].split("=", 1)[1],
        "ip": parts[3].split("=", 1)[1],
    }


def parse_firewall(line: str) -> dict | None:
    parts = line.split()
    if len(parts) < 5:
        return None
    return {"time": parts[0], "source": "firewall", "action": parts[1], "src": parts[2].split("=", 1)[1]}


def parse_web(line: str) -> dict | None:
    parts = line.split()
    if len(parts) < 4:
        return None
    return {"time": parts[0], "source": "web", "status": parts[1], "path": parts[2].split("=", 1)[1]}


def ingest() -> None:
    rows = []
    for line in (ROOT / "sample_auth.log").read_text(encoding="utf-8").splitlines():
        item = parse_auth(line)
        if item:
            rows.append(item)
    for line in (ROOT / "sample_firewall.log").read_text(encoding="utf-8").splitlines():
        item = parse_firewall(line)
        if item:
            rows.append(item)
    for line in (ROOT / "sample_web.log").read_text(encoding="utf-8").splitlines():
        item = parse_web(line)
        if item:
            rows.append(item)
    EVENTS.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    print(f"wrote {len(rows)} events")


def load() -> list[dict]:
    if not EVENTS.exists():
        raise SystemExit("run ingest first")
    return [json.loads(line) for line in EVENTS.read_text(encoding="utf-8").splitlines() if line]


def alerts() -> None:
    rows = load()
    auth_need = 5
    deny_need = 3
    probe_need = 3
    if "--auth-threshold" in sys.argv:
        auth_need = int(sys.argv[sys.argv.index("--auth-threshold") + 1])
    auth_fails = sum(1 for row in rows if row.get("source") == "auth" and row.get("action") == "FAIL")
    denies = sum(1 for row in rows if row.get("source") == "firewall" and row.get("action") == "DENY")
    probes = sum(1 for row in rows if row.get("source") == "web" and row.get("status") == "404")
    print(f"counts auth_fail={auth_fails} firewall_deny={denies} web_404={probes}")
    if auth_fails >= auth_need:
        print(f"alert auth failures={auth_fails}")
    if denies >= deny_need:
        print(f"alert firewall denies={denies}")
    if probes >= probe_need:
        print(f"alert web 404 probes={probes}")
    if auth_fails < auth_need and denies < deny_need and probes < probe_need:
        print("no alerts at these thresholds")


def search(term: str) -> None:
    hits = 0
    for row in load():
        if term.lower() in json.dumps(row).lower():
            print(json.dumps(row))
            hits += 1
    print(f"{hits} hits")


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python siem.py ingest | alerts | search TERM")
        sys.exit(1)
    if sys.argv[1] == "ingest":
        ingest()
    elif sys.argv[1] == "alerts":
        alerts()
        return
    elif sys.argv[1] == "search" and len(sys.argv) == 3:
        search(sys.argv[2])
    else:
        print("usage: python siem.py ingest | alerts | search TERM")
        sys.exit(1)


if __name__ == "__main__":
    main()
