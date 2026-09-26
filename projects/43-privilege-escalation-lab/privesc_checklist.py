"""Print enumeration commands for a lab VM you own."""

from __future__ import annotations

import sys

LINUX = [
    "id",
    "sudo -l",
    "find / -perm -4000 -type f 2>/dev/null   # SUID files",
    "ls -la /etc/cron*   # scheduled jobs",
    "ss -tulpn   # listening ports",
]

WINDOWS = [
    "whoami /priv",
    "systeminfo",
    "net start",
    "Get-Service | Where-Object Status -eq Running",
    "Get-LocalGroupMember Administrators",
]


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"linux", "windows"}:
        print("usage: python privesc_checklist.py linux|windows")
        sys.exit(1)
    print("Lab VMs only. These commands read the machine you already sit on.")
    rows = LINUX if sys.argv[1] == "linux" else WINDOWS
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
