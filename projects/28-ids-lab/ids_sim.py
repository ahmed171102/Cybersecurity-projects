"""Alert on two sample ports. Pass ordinary HTTPS. No live traffic."""

from __future__ import annotations

EVENTS = [
    {"src": "203.0.113.10", "dst": "10.0.0.5", "proto": "TCP", "port": 23},
    {"src": "203.0.113.10", "dst": "10.0.0.5", "proto": "TCP", "port": 445},
    {"src": "192.168.1.20", "dst": "10.0.0.8", "proto": "TCP", "port": 443},
]
WATCH = {23: "clear-text remote administration", 445: "file sharing"}


def main() -> None:
    for event in EVENTS:
        reason = WATCH.get(event["port"])
        if reason:
            print(f"alert {event['proto']}/{event['port']} {reason} from {event['src']}")
        else:
            print(f"pass {event['proto']}/{event['port']} from {event['src']}")


if __name__ == "__main__":
    main()
