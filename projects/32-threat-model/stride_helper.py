"""Print the six STRIDE letters for the notes app."""

from __future__ import annotations

import sys

ROWS = [
    ("S", "Spoofing", "Someone else signs in as demo. Control: password hash and a session."),
    ("T", "Tampering", "A forged form posts a note. Control: the CSRF field."),
    ("R", "Repudiation", "A user says they never saved a note. Control: keep the owner on each row."),
    ("I", "Information disclosure", "One user reads another's notes. Control: WHERE owner = ?."),
    ("D", "Denial of service", "A huge note fills the disk. Control: limit the body length before you go further."),
    ("E", "Elevation of privilege", "A normal user reaches an admin action. Control: roles, as in project 23."),
]


def main() -> None:
    print("STRIDE for projects/31-secure-webapp")
    wanted = None
    if "--letter" in sys.argv:
        wanted = sys.argv[sys.argv.index("--letter") + 1].upper()
    for letter, name, note in ROWS:
        if wanted and letter != wanted:
            continue
        print(f"{letter}  {name} — {note}")


if __name__ == "__main__":
    main()
