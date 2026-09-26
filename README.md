# Cybersecurity projects

Learning labs for Ahmed Adel Sayed Goda. Each folder is one small project you can run, explain, and put on a portfolio. The code stays short on purpose.

Five projects belong on a CV. The other 47 are practice. Do not list all 52.

| CV project | What it proves |
| --- | --- |
| `projects/23-zerotrust-api` | Short-lived tokens and role checks on an API |
| `projects/31-secure-webapp` | Hashed passwords, CSRF, and safe SQL |
| `projects/32-threat-model` | STRIDE for that notes app |
| `projects/35-secure-devops` | A build that fails on a hard-coded secret |
| `projects/49-api-security-lab` | An insecure object reference, and the fix |

Details are in `docs/CAREER.md`.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$(pwd)
python3 scripts/smoke_test.py
```

On Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:PYTHONPATH = (Get-Location).Path
python scripts\smoke_test.py
```

`python scripts/smoke_test.py` must finish with `failed: 0`. Exact demo commands are in `docs/HOW_TO_RUN.md`.

## Folder map

| Path | What it is |
| --- | --- |
| `projects/01`–`06` | Addresses, packets, DNS, subnets, a lab port scan |
| `projects/07`–`12`, `24`, `25` | Encryption, hashing, backups, roles, privacy |
| `projects/13`–`15`, `17`, `18`, `23`, `27`, `31`, `32`, `34`, `38` | Defense, the secure notes app, and the capstone |
| `projects/39`–`52` | Authorized testing workflow, reports, and detection mapping |
| `shared/crypto_utils.py` | AES-GCM helpers used by projects 07, 09, 10, 11, 24, and 26 |
| `docs/` | Concepts, tooling, Kali map, career notes, and a one-line list of all 52 |

The week-by-week order is `LEARNING_PATH.md`. Start from zero with `ZERO_TO_HERO.md`.

## Ethics rule

Only test systems you own, or systems where you have written permission. Scanners in this repo refuse public internet addresses. Password-cracking practice uses hashes the script creates itself. There is no malware and no real phishing page. Legal practice sites are listed in `ETHICAL_HACKING_GUIDE.md`.
