"""Ping a lab target and write metrics.csv. Public addresses are refused."""

from __future__ import annotations

import argparse
import csv
import ipaddress
import platform
import socket
import subprocess
import sys
from pathlib import Path


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


def ping_once(host: str) -> str:
    flag = "-n" if platform.system() == "Windows" else "-c"
    completed = subprocess.run(
        ["ping", flag, "1", host],
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        return "missing"
    for token in completed.stdout.replace("=", " ").split():
        if token.lower().startswith("time") and token[-2:].lower() == "ms":
            return token
        if token.endswith("ms") and token[:-2].replace(".", "", 1).isdigit():
            return token[:-2]
    return "missing"


def main() -> None:
    parser = argparse.ArgumentParser(description="Ping a loopback or private host.")
    parser.add_argument("--target", default="127.0.0.1")
    parser.add_argument("--count", type=int, default=3)
    parser.add_argument("--threshold", type=float, default=100.0)
    parser.add_argument("--out", default="metrics.csv")
    args = parser.parse_args()
    if not is_lab(args.target):
        print("refusing public target; use 127.0.0.1 or a private lab address")
        sys.exit(2)
    rows = []
    for index in range(1, args.count + 1):
        sample = ping_once(args.target)
        rows.append({"try": index, "target": args.target, "latency_ms": sample})
        if sample == "missing" or (sample != "missing" and float(sample) > args.threshold):
            print(f"alert try {index}: latency {sample} threshold {args.threshold}")
        else:
            print(f"ok try {index}: {sample} ms")
    with Path(args.out).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["try", "target", "latency_ms"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
