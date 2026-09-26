"""Print the sample lab and write a Mermaid diagram beside this file."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SAMPLE = ROOT / "sample_lab.json"
DIAGRAM = ROOT / "diagram.mmd"


def render(lab: dict) -> str:
    lines = [
        f"Lab: {lab['name']}",
        "",
        f"{'name':<12} {'zone':<10} {'address':<16} note",
    ]
    for device in lab["devices"]:
        lines.append(
            f"{device['name']:<12} {device['zone']:<10} {device['address']:<16} {device['note']}"
        )
    lines.append("")
    lines.append("Zones:")
    for name, meaning in lab["zones"].items():
        lines.append(f"- {name}: {meaning}")
    return "\n".join(lines)


def mermaid(lab: dict) -> str:
    lines = ["flowchart LR", "  router[router]"]
    for device in lab["devices"]:
        if device["name"] == "router":
            continue
        node = device["name"].replace("-", "_")
        lines.append(f"  router --> {node}[{device['name']} {device['zone']}]")
    return "\n".join(lines) + "\n"


def main() -> None:
    if "--sample" not in sys.argv:
        print("usage: python map_network.py --sample")
        sys.exit(1)
    lab = json.loads(SAMPLE.read_text(encoding="utf-8"))
    print(render(lab))
    DIAGRAM.write_text(mermaid(lab), encoding="utf-8")
    print(f"\nwrote {DIAGRAM.name}")


if __name__ == "__main__":
    main()
