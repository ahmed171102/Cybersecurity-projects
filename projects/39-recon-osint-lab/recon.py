"""Passive DNS, or a few local ports. Public hosts stay blocked unless you log authorization."""

from __future__ import annotations

import argparse
import ipaddress
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path

LOG = Path(__file__).resolve().parent / "engagement_log.txt"
LOCAL_PORTS = (22, 80, 443, 8080)


def is_lab(host: str) -> bool:
    try:
        addresses = [ipaddress.ip_address(host)]
    except ValueError:
        try:
            infos = socket.getaddrinfo(host, None)
        except socket.gaierror:
            return False
        addresses = [ipaddress.ip_address(info[4][0].split("%")[0]) for info in infos]
    return bool(addresses) and all(ip.is_loopback or ip.is_private for ip in addresses)


def dns_lookup(domain: str) -> None:
    print(f"passive DNS for {domain}")
    try:
        infos = socket.getaddrinfo(domain, None)
    except socket.gaierror as exc:
        print(f"no answer: {exc}")
        return
    seen = sorted({info[4][0] for info in infos})
    for address in seen:
        print(f"A/AAAA {address}")


def probe(host: str) -> None:
    print(f"local-services on {host}")
    for port in LOCAL_PORTS:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.3)
            result = sock.connect_ex((host, port))
        print(f"{host}:{port} {'open' if result == 0 else 'closed'}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive recon or lab-only port checks.")
    parser.add_argument("--domain")
    parser.add_argument("--passive", action="store_true")
    parser.add_argument("--target")
    parser.add_argument("--local-services", action="store_true")
    parser.add_argument("--i-have-authorization", action="store_true")
    args = parser.parse_args()
    if args.passive and args.domain:
        dns_lookup(args.domain)
        return
    if args.local_services and args.target:
        if not is_lab(args.target) and not args.i_have_authorization:
            print(f"refusing {args.target}: not loopback or private. Pass --i-have-authorization only with written scope.")
            sys.exit(2)
        if args.i_have_authorization:
            with LOG.open("a", encoding="utf-8") as handle:
                handle.write(f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} authorized local-services {args.target}\n")
        probe(args.target)
        return
    print("usage: python recon.py --domain example.com --passive")
    print("       python recon.py --target 127.0.0.1 --local-services")
    sys.exit(1)


if __name__ == "__main__":
    main()
