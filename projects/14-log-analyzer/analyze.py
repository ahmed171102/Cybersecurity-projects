"""Flag any IP with 5 or more FAIL lines."""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python analyze.py sample_auth.log [--threshold 5]")
        sys.exit(1)
    threshold = 5
    if "--threshold" in sys.argv:
        threshold = int(sys.argv[sys.argv.index("--threshold") + 1])
    fails: Counter[str] = Counter()
    oks: Counter[str] = Counter()
    for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if len(parts) < 4 or "=" not in parts[3]:
            continue
        status = parts[1]
        ip = parts[3].split("=", 1)[1]
        if status == "FAIL":
            fails[ip] += 1
        elif status == "OK":
            oks[ip] += 1
    print(f"threshold={threshold}  fail_ips={len(fails)}  ok_ips={len(oks)}")
    alerts = [ip for ip, count in fails.items() if count >= threshold]
    if not alerts:
        print("no alerts")
        return
    for ip in alerts:
        print(f"alert {ip} failures={fails[ip]}")


if __name__ == "__main__":
    main()
