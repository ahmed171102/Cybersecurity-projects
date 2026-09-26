#!/usr/bin/env python3
"""Run the offline labs. Exits 1 if any check fails."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable

CHECKS: list[tuple[str, list[str], str | None, tuple[int, ...]]] = [
    ("01 map", ["projects/01-network-map/map_network.py", "--sample"], "laptop", (0,)),
    ("02 packets", ["projects/02-packet-capture-lab/generate_synthetic_pcap_notes.py"], "example.com", (0,)),
    ("05 subnet", ["projects/05-subnet-calculator/subnet.py", "192.168.1.10/24", "--binary"], "255.255.255.0", (0,)),
    ("06 scan", ["projects/06-port-scanner/scanner.py", "127.0.0.1", "--ports", "1-20"], "127.0.0.1", (0,)),
    ("06 refuse public", ["projects/06-port-scanner/scanner.py", "8.8.8.8", "--ports", "80"], "refusing", (2,)),
    ("08 password", ["projects/08-password-checker/check_password.py", "--password", "Summer2024!"], "score", (0,)),
    ("12 rbac", ["projects/12-rbac-demo/rbac.py", "--user", "alice", "--action", "delete_users"], "ALLOW", (0,)),
    ("14 logs", ["projects/14-log-analyzer/analyze.py", "projects/14-log-analyzer/sample_auth.log"], "203.0.113.10", (0,)),
    ("17 firewall", ["projects/17-firewall-lab/policy_sim.py"], "3389", (0,)),
    ("18 harden", ["projects/18-linux-hardening/harden_check.py"], "user", (0,)),
    ("25 gdpr", ["projects/25-privacy-gdpr/privacy.py", "seed"], "user_1", (0,)),
    ("27 ingest", ["projects/27-siem-lite/siem.py", "ingest"], "events", (0,)),
    ("27 alerts", ["projects/27-siem-lite/siem.py", "alerts"], "auth", (0,)),
    ("28 ids", ["projects/28-ids-lab/ids_sim.py"], "445", (0,)),
    ("29 timeline", ["projects/29-incident-response/timeline_builder.py"], "2026-09-26", (0,)),
    ("32 stride", ["projects/32-threat-model/stride_helper.py"], "Spoofing", (0,)),
    ("35 gate", ["projects/35-secure-devops/security_gate.py"], "no hard-coded", (0,)),
    ("36 forensics", ["projects/36-network-forensics/investigate.py"], "203.0.113.77", (0,)),
    ("38 capstone", ["projects/38-capstone-secure-smb/checklist.py"], "SIEM", (0,)),
    ("40 triage", ["projects/40-vuln-scanning-lab/triage.py"], "P1", (0,)),
    ("41 owasp", ["projects/41-web-exploitation-lab/owasp_tracker.py", "--done", "A01,A03"], "A01", (0,)),
    ("42 crack", ["projects/42-password-cracking-lab/crack_demo.py"], "salt", (0,)),
    ("43 linux", ["projects/43-privilege-escalation-lab/privesc_checklist.py", "linux"], "sudo -l", (0,)),
    ("44 ad", ["projects/44-active-directory-lab/ad_concepts.py"], "Kerberoasting", (0,)),
    ("45 wifi", ["projects/45-wireless-security-lab/wifi_hardening.py"], "WPA3", (0,)),
    ("47 mobile", ["projects/47-mobile-app-security-lab/mobile_checklist.py"], "TLS", (0,)),
    (
        "48 iam",
        ["projects/48-cloud-security-lab/iam_lint.py", "projects/48-cloud-security-lab/sample_policy.json"],
        "IAM findings",
        (1,),
    ),
    (
        "50 report",
        ["projects/50-pentest-report-engagement/build_report.py", "--client", "Northwind", "--tester", "Ahmed Adel"],
        "Northwind",
        (0,),
    ),
    ("51 list", ["projects/51-ctf-practice-tracker/ctf_tracker.py", "list"], "challenge", (0,)),
    ("52 map", ["projects/52-purple-team-detection-map/attack_map.py", "--tactic"], "phishing", (0,)),
]


def child_env() -> dict[str, str]:
    found = os.environ.copy()
    found["PYTHONPATH"] = str(ROOT) + os.pathsep + found.get("PYTHONPATH", "")
    return found


def run(name: str, args: list[str], needle: str | None, ok_codes: tuple[int, ...]) -> bool:
    completed = subprocess.run(
        [PY, *args],
        cwd=ROOT,
        env=child_env(),
        capture_output=True,
        text=True,
    )
    output = completed.stdout + completed.stderr
    passed = completed.returncode in ok_codes and (needle is None or needle in output)
    print(f"{'PASS' if passed else 'FAIL'}  {name}")
    if not passed:
        print(output[-1500:])
    return passed


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {relative}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def crypto_checks() -> bool:
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        sample = folder / "note.txt"
        sample.write_text("portfolio lab", encoding="utf-8")
        hashed = subprocess.run(
            [PY, "projects/10-hashing-demo/hash_demo.py", "hash", str(sample)],
            cwd=ROOT,
            env=child_env(),
            capture_output=True,
            text=True,
        )
        digest = hashed.stdout.strip().split()[-1]
        verified = subprocess.run(
            [PY, "projects/10-hashing-demo/hash_demo.py", "verify", str(sample), digest],
            cwd=ROOT,
            env=child_env(),
            capture_output=True,
            text=True,
        )
        passed = hashed.returncode == 0 and verified.returncode == 0 and len(digest) == 64
        print(f"{'PASS' if passed else 'FAIL'}  10 hash")
        ok = ok and passed

        blob = folder / "note.enc"
        plain = folder / "note.out"
        encrypted = subprocess.run(
            [
                PY,
                "projects/07-file-encryptor/encryptor.py",
                "encrypt",
                "--password",
                "lab-password",
                "--in",
                str(sample),
                "--out",
                str(blob),
            ],
            cwd=ROOT,
            env=child_env(),
            capture_output=True,
            text=True,
        )
        decrypted = subprocess.run(
            [
                PY,
                "projects/07-file-encryptor/encryptor.py",
                "decrypt",
                "--password",
                "lab-password",
                "--in",
                str(blob),
                "--out",
                str(plain),
            ],
            cwd=ROOT,
            env=child_env(),
            capture_output=True,
            text=True,
        )
        passed = (
            encrypted.returncode == 0
            and decrypted.returncode == 0
            and plain.read_text(encoding="utf-8") == "portfolio lab"
        )
        print(f"{'PASS' if passed else 'FAIL'}  07 encrypt")
        if not passed:
            print(encrypted.stdout + encrypted.stderr + decrypted.stdout + decrypted.stderr)
        ok = ok and passed

        dest = folder / "backup"
        created = subprocess.run(
            [
                PY,
                "projects/11-backup-integrity/backup.py",
                "create",
                "projects/11-backup-integrity/sample_data",
                str(dest),
            ],
            cwd=ROOT,
            env=child_env(),
            capture_output=True,
            text=True,
        )
        checked = subprocess.run(
            [PY, "projects/11-backup-integrity/backup.py", "verify", str(dest)],
            cwd=ROOT,
            env=child_env(),
            capture_output=True,
            text=True,
        )
        passed = created.returncode == 0 and checked.returncode == 0 and "ok" in checked.stdout.lower()
        print(f"{'PASS' if passed else 'FAIL'}  11 backup")
        if not passed:
            print(created.stdout + created.stderr + checked.stdout + checked.stderr)
        ok = ok and passed
    return ok


def api_checks() -> bool:
    ok = True
    zt = load_module("zt_app", "projects/23-zerotrust-api/app.py")
    client = zt.app.test_client()
    alice = client.post("/login", json={"username": "alice", "password": "alicepass"})
    bob = client.post("/login", json={"username": "bob", "password": "bobpass"})
    alice_token = alice.get_json()["token"]
    bob_token = bob.get_json()["token"]
    admin = client.get("/admin/stats", headers={"Authorization": f"Bearer {alice_token}"})
    blocked = client.get("/admin/stats", headers={"Authorization": f"Bearer {bob_token}"})
    reports = client.get("/reports", headers={"Authorization": f"Bearer {bob_token}"})
    passed = alice.status_code == 200 and admin.status_code == 200 and blocked.status_code == 403 and reports.status_code == 200
    print(f"{'PASS' if passed else 'FAIL'}  23 api")
    ok = ok and passed

    notes = load_module("notes_app", "projects/31-secure-webapp/app.py")
    web = notes.app.test_client()
    page = web.get("/login")
    logged = web.post("/login", data={"username": "demo", "password": "demo-pass-123"}, follow_redirects=True)
    with web.session_transaction() as session_data:
        csrf = session_data["csrf"]
    added = web.post("/notes", data={"body": "lab note", "csrf": csrf}, follow_redirects=True)
    passed = page.status_code == 200 and logged.status_code == 200 and b"lab note" in added.data
    print(f"{'PASS' if passed else 'FAIL'}  31 webapp")
    if not passed:
        print(added.status_code, added.data[:300])
    ok = ok and passed

    subprocess.run(
        [PY, "projects/34-soc-dashboard/build_sample_alerts.py"],
        cwd=ROOT,
        env=child_env(),
        check=True,
    )
    soc = load_module("soc_app", "projects/34-soc-dashboard/app.py")
    board = soc.app.test_client()
    home = board.get("/")
    saved = board.post("/alert/1", data={"status": "triaging"}, follow_redirects=True)
    passed = home.status_code == 200 and b"HIGH" in home.data and saved.status_code == 200
    print(f"{'PASS' if passed else 'FAIL'}  34 dashboard")
    ok = ok and passed

    idor = load_module("idor_app", "projects/49-api-security-lab/vulnerable_api.py")
    api = idor.app.test_client()
    leaked = api.get("/account/bob", headers={"X-User": "alice"})
    denied = api.get("/secure/account/bob", headers={"X-User": "alice"})
    allowed = api.get("/secure/account/alice", headers={"X-User": "alice"})
    passed = leaked.status_code == 200 and denied.status_code == 403 and allowed.status_code == 200
    print(f"{'PASS' if passed else 'FAIL'}  49 idor")
    return ok and passed


def main() -> None:
    sys.path.insert(0, str(ROOT))
    os.environ["PYTHONPATH"] = str(ROOT) + os.pathsep + os.environ.get("PYTHONPATH", "")
    results = [run(name, args, needle, codes) for name, args, needle, codes in CHECKS]
    results.append(crypto_checks())
    results.append(api_checks())
    failed = sum(1 for item in results if not item)
    print(f"\nfailed: {failed}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
