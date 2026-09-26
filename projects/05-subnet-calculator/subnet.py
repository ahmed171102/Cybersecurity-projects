"""Explain a CIDR block. Optional binary view of the address and the mask."""

from __future__ import annotations

import ipaddress
import sys


def binary(ip: ipaddress.IPv4Address | ipaddress.IPv6Address) -> str:
    if isinstance(ip, ipaddress.IPv6Address):
        return format(int(ip), "0128b")
    return ".".join(f"{int(part):08b}" for part in str(ip).split("."))


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python subnet.py 192.168.1.10/24 --binary")
        sys.exit(1)
    try:
        network = ipaddress.ip_network(sys.argv[1], strict=False)
    except ValueError as exc:
        print(exc)
        sys.exit(1)
    print(f"input:     {sys.argv[1]}")
    print(f"network:   {network.network_address}")
    print(f"broadcast: {network.broadcast_address}")
    print(f"mask:      {network.netmask}")
    print(f"wildcard:  {network.hostmask}")
    if network.version == 4 and network.prefixlen <= 30:
        hosts = list(network.hosts())
        print(f"usable:    {len(hosts)} ({hosts[0]} - {hosts[-1]})")
    else:
        print(f"addresses: {network.num_addresses}")
    if "--binary" in sys.argv and network.version == 4:
        print(f"address binary: {binary(ipaddress.ip_address(sys.argv[1].split('/')[0]))}")
        print(f"mask binary:    {binary(ipaddress.ip_address(str(network.netmask)))}")


if __name__ == "__main__":
    main()
