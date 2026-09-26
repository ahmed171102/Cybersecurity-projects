"""Read-only host notes. This script does not change settings."""

from __future__ import annotations

import getpass
import os
import platform
import shutil
from pathlib import Path


def line(label: str, value: str) -> None:
    print(f"{label}: {value}")


def sshd_notes() -> None:
    path = Path("/etc/ssh/sshd_config")
    if not path.is_file():
        line("sshd", "config not readable on this machine")
        return
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    interesting = [
        raw.strip()
        for raw in text
        if raw.strip() and not raw.strip().startswith("#") and raw.split()[0] in {"PermitRootLogin", "PasswordAuthentication", "Port"}
    ]
    line("sshd", "; ".join(interesting) if interesting else "no PermitRootLogin/PasswordAuthentication/Port lines set")


def main() -> None:
    line("user", getpass.getuser())
    if hasattr(os, "geteuid"):
        line("root", "yes" if os.geteuid() == 0 else "no")
    else:
        line("root", "not applicable on this OS (check the Linux lab VM)")
    line("ufw", shutil.which("ufw") or "not on PATH")
    line("ssh", shutil.which("ssh") or "not on PATH")
    line("kernel", platform.platform())
    sshd_notes()
    print("read-only check finished")


if __name__ == "__main__":
    main()
