"""TCP connect scan for loopback and private lab addresses only."""

from __future__ import annotations

import argparse
import ipaddress
import socket
import sys

COMMON = (22, 80, 443, 445, 3306, 3389, 5001, 5002, 5003, 5005, 8080)


def is_lab(host: str) -> bool:
    try:
        addresses = [ipaddress.ip_address(host)]
    except ValueError:
        try:
            infos = socket.getaddrinfo(host, None)
        except socket.gaierror:
            return False
        addresses = []
        for info in infos:
            addresses.append(ipaddress.ip_address(info[4][0].split("%")[0]))
    return bool(addresses) and all(ip.is_loopback or ip.is_private for ip in addresses)


def parse_ports(text: str | None) -> list[int]:
    if not text:
        return list(COMMON)
    ports: list[int] = []
    for piece in text.split(","):
        if "-" in piece:
            start, end = piece.split("-", 1)
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(piece))
    return ports


def main() -> None:
    parser = argparse.ArgumentParser(description="Connect-scan a lab host.")
    parser.add_argument("host", nargs="?", default="127.0.0.1")
    parser.add_argument("--ports", help="80,443 or 1-20. Default is a short common list.")
    args = parser.parse_args()
    if not is_lab(args.host):
        print(f"refusing {args.host}: scanners in this repo stay on loopback or private lab addresses")
        sys.exit(2)
    ports = parse_ports(args.ports)
    print(f"target {args.host} is loopback or private; scan allowed")
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.2)
            result = sock.connect_ex((args.host, port))
        if result == 0:
            open_ports.append(port)
            print(f"{args.host}:{port} open")
        else:
            print(f"{args.host}:{port} closed")
    print("open ports: " + (", ".join(str(port) for port in open_ports) or "none"))


if __name__ == "__main__":
    main()
