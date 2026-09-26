"""Draw a hop path. If traceroute is missing, write a synthetic 4-hop diagram."""

from __future__ import annotations

import platform
import shutil
import subprocess
import sys
from pathlib import Path

DIAGRAM = Path(__file__).resolve().parent / "path.mmd"
SYNTHETIC = ["127.0.0.1 you", "192.168.1.1 gateway", "203.0.113.1 lab router", "203.0.113.10 lab host"]


def command_for(target: str) -> list[str] | None:
    if platform.system() == "Windows" and shutil.which("tracert"):
        return ["tracert", "-d", "-h", "8", target]
    if shutil.which("traceroute"):
        return ["traceroute", "-n", "-m", "8", target]
    if shutil.which("tracepath"):
        return ["tracepath", "-n", target]
    return None


def write_diagram(hops: list[str]) -> None:
    lines = ["flowchart LR"]
    for index, hop in enumerate(hops):
        node = f"h{index}"
        lines.append(f"  {node}[{hop}]")
        if index:
            lines.append(f"  h{index - 1} --> {node}")
    DIAGRAM.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    command = command_for(target)
    if command is None or target != "127.0.0.1":
        print("traceroute tool missing or target is not loopback; printing a synthetic 4-hop path")
        for hop in SYNTHETIC:
            print(hop)
        write_diagram(SYNTHETIC)
        print(f"wrote {DIAGRAM.name}")
        return
    completed = subprocess.run(command, capture_output=True, text=True)
    print(completed.stdout or completed.stderr)
    hops = [line.strip() for line in (completed.stdout or "").splitlines() if line.strip()][:8]
    write_diagram(hops or SYNTHETIC)
    print(f"wrote {DIAGRAM.name}")


if __name__ == "__main__":
    main()
