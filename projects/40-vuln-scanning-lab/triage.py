"""Rank sample findings. Scanners belong on lab VMs you own."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VALUES = {"low": 1.0, "medium": 1.3, "high": 1.6}


def band(score: float) -> str:
    if score >= 15:
        return "P1"
    if score >= 9:
        return "P2"
    if score >= 5:
        return "P3"
    return "P4"


def main() -> None:
    findings = json.loads((ROOT / "findings.json").read_text(encoding="utf-8"))
    ranked = []
    for item in findings:
        score = item["cvss"]
        if item["exploit"]:
            score += 2
        score *= VALUES[item["asset_value"]]
        ranked.append((score, band(score), item))
    ranked.sort(reverse=True)
    print("Priority = CVSS, plus 2 if an exploit exists, times asset value.")
    for score, label, item in ranked:
        print(f"{label}  {score:.1f}  {item['id']}  {item['title']}")
    print("Run scanners only on lab VMs you own.")


if __name__ == "__main__":
    main()
