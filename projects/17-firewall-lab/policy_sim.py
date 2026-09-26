"""First-match firewall. LAN SSH is allowed. Public SSH and 3389 are not. Public 80 is allowed."""

from __future__ import annotations

import ipaddress

LAN = ipaddress.ip_network("192.168.1.0/24")

# Each rule is action, port, source network or None for any.
RULES = [
    ("ALLOW", 22, LAN, "LAN SSH"),
    ("DENY", 22, None, "public SSH"),
    ("ALLOW", 80, None, "public HTTP"),
    ("DENY", 3389, None, "remote desktop closed"),
    ("DENY", None, None, "default deny"),
]

CASES = [
    ("192.168.1.20", 22),
    ("203.0.113.8", 22),
    ("203.0.113.8", 80),
    ("198.51.100.9", 3389),
    ("192.168.1.20", 443),
]


def matches(rule: tuple, source: str, port: int) -> bool:
    action, rule_port, network, _why = rule
    del action
    if rule_port is not None and rule_port != port:
        return False
    if network is not None and ipaddress.ip_address(source) not in network:
        return False
    return True


def decide(source: str, port: int) -> tuple[str, str]:
    for rule in RULES:
        if matches(rule, source, port):
            return rule[0], rule[3]
    return "DENY", "no match"


def main() -> None:
    print("First match wins. A later deny never runs if an earlier allow already matched.\n")
    print("Rules:")
    for action, port, network, why in RULES:
        src = str(network) if network else "any"
        port_text = str(port) if port is not None else "any"
        print(f"  {action} src={src} port={port_text}  ({why})")
    print()
    for source, port in CASES:
        action, why = decide(source, port)
        print(f"{source} -> tcp/{port} : {action} ({why})")
    print("\nLAN HTTPS (443) hits default deny on purpose. Add an allow if the lab web server needs it.")


if __name__ == "__main__":
    main()
