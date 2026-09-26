# Ahmed’s learning path

Personal study order for **Ahmed Adel Sayed Goda**, Cairo. Computer Engineering, AASTMT, 2021–2026. Backend and AI internship work on secure APIs. Network internship work on Cisco firewalls, Wireshark, and Nmap. Current study: SOC, networks, and ethical hacking.

This file is enough on its own. You do not need the other docs to start. If `docs/KALI_LINUX.md` exists later, read it before you install Kali. Other people own `LEARNING_PATH.md` and that Kali note. Leave those files alone.

Repo root (every command below starts here):

`M:\Term 10\My Projects\Cybersecurity-projects`

---

## How to use this file

One sitting is one lab, not a whole week.

1. Pick the next folder in the week you are on.
2. Set `PYTHONPATH` to the repo root (see setup below).
3. Run the command in this file.
4. Change **one** setting or input (a different subnet, a different user, a wrong password, a public address that should be refused).
5. Write **three sentences**: what ran, what changed when you changed that one thing, and what you would tell a teammate.

Stop when the three sentences are written. Do not stack three folders in one evening to “catch up.” Forgetting a lecture detail is normal. The three sentences are the part that stays.

Test only what you own, a classroom VM, or a platform that already named the target. Written permission only. Do not scan the public internet.

---

## One-time setup

PowerShell, from the repo root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt --maxsockets=2
$env:PYTHONPATH = (Get-Location).Path
```

`PYTHONPATH` must be the repo root every time you open a new terminal. Projects 07, 09, 10, 11, 24, and 26 import `shared.crypto_utils`. Set the variable anyway.

On this machine, `python` is the usual command. If a README says `python3`, use `python`.

Optional check that the repo still runs:

```powershell
python scripts/smoke_test.py
```

Done when the last line says `failed: 0`.

---

## 12-week core

### Weeks 1–4 — networks

Projects `01`–`06`. Pair this month with what you already did on Cisco gear, Wireshark, and Nmap. The point is to name a subnet, a handshake, and an open port in your own words.

#### Week 1 — map and packets

**`projects/01-network-map`**

```powershell
python projects/01-network-map/map_network.py --sample
```

Done: the table printed, `diagram.mmd` exists, and you can say why the IoT bulb must not start a connection to the laptop.

**`projects/02-packet-capture-lab`**

```powershell
python projects/02-packet-capture-lab/generate_synthetic_pcap_notes.py
```

Done: you read the 7-packet story (ping, DNS, TCP handshake) and filled the worksheet from a short capture on a machine you own. Capture only networks you own.

#### Week 2 — TCP and DNS

**`projects/03-tcp-chat`**

```powershell
python projects/03-tcp-chat/server.py
```

Second and third terminals:

```powershell
python projects/03-tcp-chat/client.py
```

Done: two clients talk on `127.0.0.1:9000`, and you wrote why the server binds to loopback, not every interface.

**`projects/04-dns-resolver`**

```powershell
python projects/04-dns-resolver/resolve.py example.com
```

Done: you can point at the A record a browser uses and the MX record mail uses.

#### Week 3 — subnets

**`projects/05-subnet-calculator`**

```powershell
python projects/05-subnet-calculator/subnet.py 192.168.1.10/24 --binary
```

Change one setting: run the same address with `/26`.

Done: you have both outputs and one sentence on why `/26` has fewer hosts. This is the same skill as reading a Cisco interface mask.

#### Week 4 — local port check

**`projects/06-port-scanner`**

```powershell
python projects/06-port-scanner/scanner.py 127.0.0.1 --ports 1-20
python projects/06-port-scanner/scanner.py 8.8.8.8 --ports 80
```

Done: you have output from your own machine, the second command refused the public address and exited 2, and you wrote what “open” means. Do not point this (or Nmap) at the public internet.

After week 4, set up the Kali stage below. Do not start authorized testing until that lab is isolated and snapshotted.

---

### Weeks 5–8 — data security

Projects `07`–`12`, then `24` and `25`. Encryption, hashes, backups, roles, secrets, and a privacy delete.

#### Week 5 — encrypt and score a password

**`projects/07-file-encryptor`**

```powershell
python projects/07-file-encryptor/encryptor.py encrypt --password "lab-password" --in notes.txt --out notes.enc
python projects/07-file-encryptor/encryptor.py decrypt --password "lab-password" --in notes.enc --out notes.out
```

Done: `notes.enc` is unreadable, `notes.out` matches the original, and you mentioned the 200,000 PBKDF2 iterations.

**`projects/08-password-checker`**

```powershell
python projects/08-password-checker/check_password.py --password "Summer2024!"
```

Change one setting: run it again with `password`.

Done: two scores side by side and one sentence on why a longer passphrase scores higher. The password stays on this machine.

#### Week 6 — vault and hash

**`projects/09-secure-notes`**

```powershell
python projects/09-secure-notes/notes.py init --password "lab-password"
python projects/09-secure-notes/notes.py add --password "lab-password" --title wifi --body "lab only"
python projects/09-secure-notes/notes.py list --password "lab-password"
python projects/09-secure-notes/notes.py get --password "lab-password" --title wifi
```

Done: `vault.enc` looks random in a text editor, and `get` prints the note only with the right password.

**`projects/10-hashing-demo`**

```powershell
python projects/10-hashing-demo/hash_demo.py hash README.md
python projects/10-hashing-demo/hash_demo.py verify README.md PASTE_THE_DIGEST
```

Change one setting: copy the file, change one character, hash again.

Done: you have two digests and you can say a hash is not decrypted.

#### Week 7 — backup and roles

**`projects/11-backup-integrity`**

```powershell
python projects/11-backup-integrity/backup.py create projects/11-backup-integrity/sample_data $env:TEMP\lab-backup
python projects/11-backup-integrity/backup.py verify $env:TEMP\lab-backup
```

Change one setting: edit one copied file, then verify again.

Done: first verify prints `ok`; the edited copy exits 1.

**`projects/12-rbac-demo`**

```powershell
python projects/12-rbac-demo/rbac.py --user alice --action delete_users
python projects/12-rbac-demo/rbac.py --user carol --action delete_users
```

Done: alice is allowed, carol is denied, and you added one extra action for bob only.

#### Week 8 — secrets and privacy

**`projects/24-secrets-manager`**

```powershell
python projects/24-secrets-manager/secrets.py init --password "lab-password"
python projects/24-secrets-manager/secrets.py set --password "lab-password" --name db --value "lab-only"
python projects/24-secrets-manager/secrets.py rotate --password "lab-password" --name db --value "lab-only-2"
python projects/24-secrets-manager/secrets.py audit --password "lab-password"
```

Done: the audit log shows a set and a rotate, and the screenshot has the values redacted.

**`projects/25-privacy-gdpr`**

```powershell
python projects/25-privacy-gdpr/privacy.py seed
python projects/25-privacy-gdpr/privacy.py inventory
python projects/25-privacy-gdpr/privacy.py export user_1
python projects/25-privacy-gdpr/privacy.py delete user_1
```

Done: you have the export file, and the inventory after delete shows `user_2` still there and `user_1` gone.

---

### Weeks 9–12 — defense

Projects `13`–`15`, `17`, `18`, `23`, `27`, `31`, `32`, `34`, `38`. Headers, logs, awareness, firewall, host check, a small API, a SIEM, a notes app, a threat model, a queue, then one short company story.

#### Week 9 — headers, logs, awareness

**`projects/13-webapp-security-checklist`**

```powershell
python projects/13-webapp-security-checklist/check_headers.py https://example.com
```

Done: a filled audit for a site you own or for `example.com`, with one sentence per missing header. This is a header check, not a scan of someone else’s network.

**`projects/14-log-analyzer`**

```powershell
python projects/14-log-analyzer/analyze.py projects/14-log-analyzer/sample_auth.log
```

Change one setting: add one failure from a different address and run again.

Done: the first run flags an IP after five failed logons; the extra address stays quiet.

**`projects/15-phishing-awareness`**

```powershell
cd projects/15-phishing-awareness
python -m http.server 8080
```

Open `http://127.0.0.1:8080/`. This server only shares that folder on your computer. There is no password form and no phishing kit.

Done: a screenshot of the two messages, your score, and one example you rewrote in the safer style (no real company secrets).

#### Week 10 — firewall, host, API

**`projects/17-firewall-lab`**

```powershell
python projects/17-firewall-lab/policy_sim.py
```

Done: the four simulator lines (LAN SSH allow, public SSH deny, public 80 allow, 3389 deny) and one sentence on which rule matches public SSH. Apply UFW only on a lab VM. Pair this with the Cisco internship: first match wins.

**`projects/18-linux-hardening`**

```powershell
python projects/18-linux-hardening/harden_check.py
```

Done: script output from your lab VM next to a checked copy of `CHECKLIST.md`. Read-only check. Do not “harden” a machine you do not own.

**`projects/23-zerotrust-api`** (CV project)

```powershell
python projects/23-zerotrust-api/app.py
```

Then, with the app running:

```powershell
curl -s http://127.0.0.1:5001/login -H "Content-Type: application/json" -d "{\"username\":\"alice\",\"password\":\"alicepass\"}"
```

Send the token as `Authorization: Bearer ...` to `/admin/stats` as alice, then as bob.

Done: alice gets admin stats; bob gets 403 on the same path. Lab accounts stay local. Change `JWT_SECRET` if this is not a throwaway lab.

#### Week 11 — SIEM, notes app, STRIDE

**`projects/27-siem-lite`**

```powershell
python projects/27-siem-lite/siem.py ingest
python projects/27-siem-lite/siem.py alerts
python projects/27-siem-lite/siem.py search 203.0.113.10
```

Done: three alert lines, and you can name which sample log each one came from.

**`projects/31-secure-webapp`** (CV project)

```powershell
python projects/31-secure-webapp/app.py
```

Open `http://127.0.0.1:5002/login` and sign in as `demo` / `demo-pass-123`.

Done: you saved a note, and you wrote one sentence each on the password hash, the CSRF field, and SQL placeholders.

**`projects/32-threat-model`** (CV project)

```powershell
python projects/32-threat-model/stride_helper.py
```

Done: you read `STRIDE.md` and `diagram.mmd`, and you added one extra row for a threat the current notes app does not cover yet.

#### Week 12 — queue and capstone

**`projects/34-soc-dashboard`**

```powershell
python projects/34-soc-dashboard/build_sample_alerts.py
python projects/34-soc-dashboard/app.py
```

Open `http://127.0.0.1:5003/` and move the HIGH brute-force alert from open to triaging.

Done: a screenshot of the counts after that one status change.

**`projects/38-capstone-secure-smb`**

```powershell
python projects/38-capstone-secure-smb/checklist.py
```

Done: `CAPSTONE_REPORT.md` filled in, two pages at most. One story: map, firewall, hardening, secure app, backup, SIEM, response, policy.

---

## Where the other projects sit

Nothing in `01`–`52` is leftover junk. The 12-week core is the spine. These sit after the month they belong to, or after Kali is isolated.

### After month 1 (networks) — do `19`–`22`

Same ideas as weeks 1–4, with more drawing and measurement.

| # | Folder | Command | Done |
| --- | --- | --- | --- |
| 19 | `projects/19-vlan-homelab` | Open `vlan.mmd` and read `POLICY.md` (no install) | Diagram plus one allow rule: source, destination, port |
| 20 | `projects/20-vpn-lab` | Read `wg0.conf.sample`; generate keys only on a lab VM; keep keys out of git | Write-up with tunnel address and `AllowedIPs`, private key redacted |
| 21 | `projects/21-network-monitor` | `python projects/21-network-monitor/monitor.py --target 127.0.0.1 --count 3 --threshold 100` | CSV from your machine and one sentence on what would page a person |
| 22 | `projects/22-traceroute-visualizer` | `python projects/22-traceroute-visualizer/trace.py` | `path.mmd` and your real gateway from `ipconfig` |

### After month 2 (data) — do `26`

| # | Folder | Command | Done |
| --- | --- | --- | --- |
| 26 | `projects/26-secure-file-share` | `python projects/26-secure-file-share/share.py put --password "lab-password" --file README.md` then `get` with the printed token | A successful get, then the same token after it expires |

### After month 3 (defense) — do `28`–`30`, `33`, `35`–`37`

| # | Folder | Command | Done |
| --- | --- | --- | --- |
| 28 | `projects/28-ids-lab` | `python projects/28-ids-lab/ids_sim.py` | Alerts on TCP/23 and TCP/445, pass on 443, plus one expected false positive in the write-up |
| 29 | `projects/29-incident-response` | `python projects/29-incident-response/timeline_builder.py` | Timeline plus your five answers in `TABLETOP.md` |
| 30 | `projects/30-malware-analysis-report` | Read `FICTIONAL_IOCS.md`; copy `REPORT_TEMPLATE.md` | Completed template using only fictional or lab-generated indicators; snapshot name at the top. This repo has no malware sample. |
| 33 | `projects/33-blue-team-lab` | Open `topology.mmd` and read `DETECTION.md` | Diagram screenshot and five log lines from your own isolated lab |
| 35 | `projects/35-secure-devops` (CV) | `python projects/35-secure-devops/security_gate.py` then `python projects/35-secure-devops/app_demo.py` | Green gate, then a failing run after you temporarily add `SECRET = "oops"` to a **copy** of the demo |
| 36 | `projects/36-network-forensics` | `python projects/36-network-forensics/investigate.py` | Case report that treats the 12MB upload as a fact that needs an owner, not as proof of malware |
| 37 | `projects/37-policy-architecture` | Read `POLICY.md` and open `architecture.mmd` | Four classification labels rewritten for a clinic or small shop you invent |

Project `16` is not in the 12-week core. It sits with the Kali stage (report practice).

### After Kali is isolated — do `16`, then `39`–`52`

Only on a host-only lab, a classroom VM you own, or a platform that named the target. Written permission. No public-internet scanning.

| # | Folder | Command | Done |
| --- | --- | --- | --- |
| 16 | `projects/16-vuln-lab-report` | Read `SAMPLE_FINDING.md`; copy `REPORT_TEMPLATE.md` | One finding in your own words, lab name and date, no copied walkthrough, no exploit code |
| 39 | `projects/39-recon-osint-lab` | `python projects/39-recon-osint-lab/recon.py --domain example.com --passive` then `--target 127.0.0.1 --local-services` | Passive DNS output; local-service check only on a lab host |
| 40 | `projects/40-vuln-scanning-lab` | `python projects/40-vuln-scanning-lab/triage.py` | Ranked list from `findings.json` and why a medium score on a high-value host can beat a higher score on a printer |
| 41 | `projects/41-web-exploitation-lab` | `python projects/41-web-exploitation-lab/owasp_tracker.py --done A01,A03` | Two filled write-ups in your own words. Tracker only. No payloads. |
| 42 | `projects/42-password-cracking-lab` | `python projects/42-password-cracking-lab/crack_demo.py` | The lesson line, plus why project 31 uses Werkzeug instead of MD5. Cracks only hashes the script just created. |
| 43 | `projects/43-privilege-escalation-lab` | `python projects/43-privilege-escalation-lab/privesc_checklist.py linux` | Checklist against a VM you own; `sudo -l` output and whether any command may run as root |
| 44 | `projects/44-active-directory-lab` | `python projects/44-active-directory-lab/ad_concepts.py` | Five technique names with one defense each, in your own words |
| 45 | `projects/45-wireless-security-lab` | `python projects/45-wireless-security-lab/wifi_hardening.py` | Photo of **your** AP settings (SSID blurred): WPA2-AES or WPA3, WPS off |
| 46 | `projects/46-social-engineering-awareness` | `python projects/46-social-engineering-awareness/quiz.py --demo` then `python projects/46-social-engineering-awareness/quiz.py` | Your score and one extra question you wrote about a fake delivery SMS |
| 47 | `projects/47-mobile-app-security-lab` | `python projects/47-mobile-app-security-lab/mobile_checklist.py` | Six lines (keys, storage, TLS, logs) applied to an app you wrote or a teaching app |
| 48 | `projects/48-cloud-security-lab` | `python projects/48-cloud-security-lab/iam_lint.py projects/48-cloud-security-lab/sample_policy.json` | The three findings plus a rewritten statement that allows `s3:GetObject` on one bucket |
| 49 | `projects/49-api-security-lab` (CV) | `python projects/49-api-security-lab/vulnerable_api.py` then, second terminal: `cd projects/49-api-security-lab` and `python test_idor.py` | 200 on the broken route, 403 when bob is not the owner, 200 when alice reads alice |
| 50 | `projects/50-pentest-report-engagement` | `python projects/50-pentest-report-engagement/build_report.py --client Northwind --tester "Ahmed Adel"` | Filled rules of engagement and one finding after a legal lab |
| 51 | `projects/51-ctf-practice-tracker` | `python projects/51-ctf-practice-tracker/ctf_tracker.py list` then `add` and `stats` | Stats line after ten rooms on TryHackMe or OverTheWire |
| 52 | `projects/52-purple-team-detection-map` | `python projects/52-purple-team-detection-map/attack_map.py --tactic` | A sixth row you add for “new local admin” (events 4720 and 4732) |

---

## Kali stage

Do this **after week 4** and **before** any authorized testing. The Python data and defense weeks can continue on Windows at the same time.

1. Install VirtualBox on the host.
2. Create a **host-only** network. Do not bridge Kali onto home Wi-Fi.
3. Install Kali on that network.
4. Install **OWASP Juice Shop** or **DVWA** as the only web target.
5. Take a snapshot while the pair is clean. Roll back to that snapshot when a lab gets messy.
6. If `docs/KALI_LINUX.md` exists, read it before the first boot. If it does not exist yet, wait for it or follow this section.

Capture traffic and run scanners only on that host-only network.

### First month on Kali

- TryHackMe beginner path.
- OverTheWire Bandit, levels 0–15.
- PortSwigger Web Security Academy: SQL injection, XSS, and access control, **on their site**.
- Two write-ups in your own words: what you were allowed to touch, what you observed, what you would fix. Use `projects/16-vuln-lab-report` and `projects/50-pentest-report-engagement` for the shape. Do not paste a public walkthrough.

Written permission only. A lab you installed, a platform that owns the target, or a contract that names hosts and dates. A chat message is not permission. Do not scan the public internet.

This repo does not include exploit payloads, malware, phishing kits, or attack procedures. Do not add them.

---

## Career stage

Show **five** projects on a CV, not all 52. The rest is practice you can talk about if asked.

| # | Folder | One CV bullet |
| --- | --- | --- |
| 23 | `23-zerotrust-api` | Issued short-lived JWTs for a lab API and enforced role checks so a normal user cannot read admin stats. |
| 31 | `31-secure-webapp` | Built a notes service that stores password hashes, rejects cross-site form posts, and sends SQL values as parameters instead of pasted strings. |
| 32 | `32-threat-model` | Wrote a STRIDE model for the notes app, tying spoofing, tampering, and elevation to the login, CSRF, and role controls already in the code. |
| 35 | `35-secure-devops` | Added a CI gate that fails the build when a Python file hard-codes a secret assignment. |
| 49 | `49-api-security-lab` | Reproduced an insecure direct object reference in a lab API and added an owner check that returns 403 for the same request. |

Target roles: application security, and securing AI or backend systems. Pair the network internship with projects 02, 05, 06, and 17 in one sentence: you can read a subnet, a handshake, and a firewall rule. Do not claim a production SOC you did not work in.

### Certificates later

After the 12-week core and after you can write a short report without a walkthrough:

1. CompTIA Security+
2. Cisco junior cybersecurity analyst (or the current Cisco equivalent)
3. eJPT
4. PNPT
5. OSCP **only** after you can write a report (project 50 filled from a legal lab, in your own words)

A certificate without a report is a score. The report is the job.

---

## After graduation

Forgetting lecture details after graduation is normal. You will not keep every Cisco command or every OSI layer definition in working memory. Rebuilding **one** small project from this repo — a subnet, a hash check, a failed-logon alert — brings the idea back in an evening. That is the point of keeping the folders small.

---

## Week-by-week checklist

Tick when the three sentences are written, not when the command merely exited 0.

### Setup

- [ ] Virtualenv created, `PYTHONPATH` set, `python scripts/smoke_test.py` ends with `failed: 0`

### Weeks 1–4 — networks

- [ ] Week 1: `01-network-map` — table, `diagram.mmd`, IoT sentence
- [ ] Week 1: `02-packet-capture-lab` — 7-packet story + own short capture worksheet
- [ ] Week 2: `03-tcp-chat` — two clients on loopback
- [ ] Week 2: `04-dns-resolver` — A vs MX
- [ ] Week 3: `05-subnet-calculator` — `/24` and `/26`
- [ ] Week 4: `06-port-scanner` — localhost output + public address refused
- [ ] Kali host-only lab installed, Juice Shop or DVWA up, clean snapshot taken
- [ ] Read `docs/KALI_LINUX.md` if it exists

### After month 1

- [ ] `19-vlan-homelab`
- [ ] `20-vpn-lab`
- [ ] `21-network-monitor`
- [ ] `22-traceroute-visualizer`

### Weeks 5–8 — data security

- [ ] Week 5: `07-file-encryptor`
- [ ] Week 5: `08-password-checker`
- [ ] Week 6: `09-secure-notes`
- [ ] Week 6: `10-hashing-demo`
- [ ] Week 7: `11-backup-integrity`
- [ ] Week 7: `12-rbac-demo`
- [ ] Week 8: `24-secrets-manager`
- [ ] Week 8: `25-privacy-gdpr`

### After month 2

- [ ] `26-secure-file-share`

### Weeks 9–12 — defense

- [ ] Week 9: `13-webapp-security-checklist`
- [ ] Week 9: `14-log-analyzer`
- [ ] Week 9: `15-phishing-awareness`
- [ ] Week 10: `17-firewall-lab`
- [ ] Week 10: `18-linux-hardening`
- [ ] Week 10: `23-zerotrust-api` (CV)
- [ ] Week 11: `27-siem-lite`
- [ ] Week 11: `31-secure-webapp` (CV)
- [ ] Week 11: `32-threat-model` (CV)
- [ ] Week 12: `34-soc-dashboard`
- [ ] Week 12: `38-capstone-secure-smb`

### After month 3

- [ ] `28-ids-lab`
- [ ] `29-incident-response`
- [ ] `30-malware-analysis-report` (fictional indicators only)
- [ ] `33-blue-team-lab`
- [ ] `35-secure-devops` (CV)
- [ ] `36-network-forensics`
- [ ] `37-policy-architecture`

### Kali first month (after week 4, isolated lab only)

- [ ] TryHackMe beginner path started
- [ ] OverTheWire Bandit 0–15
- [ ] PortSwigger SQLi, XSS, and access control on their site
- [ ] Two write-ups in my own words (`16` + `50` shape)

### After Kali is isolated

- [ ] `16-vuln-lab-report`
- [ ] `39-recon-osint-lab`
- [ ] `40-vuln-scanning-lab`
- [ ] `41-web-exploitation-lab`
- [ ] `42-password-cracking-lab`
- [ ] `43-privilege-escalation-lab`
- [ ] `44-active-directory-lab`
- [ ] `45-wireless-security-lab`
- [ ] `46-social-engineering-awareness`
- [ ] `47-mobile-app-security-lab`
- [ ] `48-cloud-security-lab`
- [ ] `49-api-security-lab` (CV)
- [ ] `50-pentest-report-engagement`
- [ ] `51-ctf-practice-tracker`
- [ ] `52-purple-team-detection-map`

### Career

- [ ] CV lists only 23, 31, 32, 35, 49
- [ ] Security+ / Cisco junior analyst / eJPT / PNPT considered after a real report
- [ ] OSCP not started until I can write that report
