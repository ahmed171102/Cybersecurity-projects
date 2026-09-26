"""Name five Active Directory techniques and one defense each. No attack scripts."""

from __future__ import annotations

ROWS = [
    (
        "Kerberoasting",
        "A service account's ticket can be taken offline and guessed if the password is weak.",
        "Defense: long random service passwords, or group Managed Service Accounts.",
    ),
    (
        "AS-REP roasting",
        "Accounts that do not require Kerberos pre-authentication can have a blob guessed offline.",
        "Defense: require pre-authentication. Do not leave that box unchecked for convenience.",
    ),
    (
        "Pass-the-hash",
        "A stolen NTLM hash can be reused as if it were the password.",
        "Defense: Credential Guard, least privilege, and rotate local admin passwords so they are not the same everywhere.",
    ),
    (
        "DCSync",
        "A principal that can replicate directory data can ask for password hashes as a domain controller would.",
        "Defense: almost nobody should have Replicating Directory Changes. Audit who has it.",
    ),
    (
        "Golden ticket",
        "The KRBTGT account is the key that signs tickets for a long time.",
        "Defense: protect domain controllers, and reset KRBTGT twice in a planned change if you believe it leaked.",
    ),
]


def main() -> None:
    print("Active Directory ideas for a lab you own. This file does not run any of them.\n")
    for name, meaning, defense in ROWS:
        print(name)
        print(f"  {meaning}")
        print(f"  {defense}")
        print()


if __name__ == "__main__":
    main()
