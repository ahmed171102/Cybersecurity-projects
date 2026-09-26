"""Look up common DNS record types. Query only names you are allowed to ask about."""

from __future__ import annotations

import sys

import dns.resolver

TYPES = ("A", "AAAA", "MX", "CNAME", "TXT", "NS")


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: python resolve.py example.com")
        sys.exit(1)
    name = sys.argv[1]
    print(f"DNS for {name}")
    for record_type in TYPES:
        try:
            answers = dns.resolver.resolve(name, record_type)
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            print(f"{record_type}: none")
            continue
        except dns.exception.DNSException as exc:
            print(f"{record_type}: error {exc.__class__.__name__}")
            continue
        print(f"{record_type}:")
        for item in answers:
            print(f"  {item.to_text()}")


if __name__ == "__main__":
    main()
