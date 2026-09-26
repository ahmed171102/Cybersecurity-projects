# Zero to hero

You already write Python and you have seen firewalls, Wireshark, and Nmap on a network internship. This path does not pretend you are starting from a blank page. It rebuilds the ideas in small programs so they stick.

Forgetting lecture details after graduation is normal. Rebuilding one small project brings the idea back. When a term feels gone, open the matching folder and run it once.

## Stage 0 — foundations

Read `docs/CONCEPTS.md`. Run project 05 until network, broadcast, and host count are boring. Run project 08 and say out loud why a short common password scores badly.

## Stage 1 — CIA and crypto

Confidentiality, integrity, and availability are the three words behind projects 07, 10, and 11.

- Encryption hides the bytes (project 07).
- A hash fingerprints the bytes (project 10). They are not the same job.
- A checksum file tells you the backup was not edited (project 11).

## Stage 2 — packets, firewall, VPN, lab

Projects 01, 02, 03, 04, and 06 are the network. Then read the firewall simulator (17), the VLAN rules (19), and the WireGuard placeholders (20). Build the lab in `ETHICAL_HACKING_GUIDE.md`: VirtualBox, an isolated network, a snapshot named `clean-start`.

## Stage 3 — blue team

Projects 14, 27, 28, 29, and 34 are the analyst loop: collect, alert, decide, write a timeline. Project 18 is the host checklist you run before you call a machine "done".

## Stage 4 — authorized offense

Only after stages 0–3. Read `ETHICAL_HACKING_GUIDE.md`. Use TryHackMe, Hack The Box, picoCTF, PortSwigger Web Security Academy, OverTheWire, and VulnHub. Projects 39–46 in this repo are checklists and safe demos. The targets live on those sites, or on a VM you own.

## Stage 5 — a report plus the capstone

Project 50 is the report shape. Project 49 is the API bug you should be able to demo. Project 38 ties the earlier labs into one small-company story. Project 32 is the threat model you talk through beside project 31.

## Certificates, later

Use them as a syllabus after the labs, not as a substitute.

- CompTIA Security+ for the shared vocabulary.
- A Cisco junior analyst track if you want to stay close to firewalls and packets.
- eJPT, then PNPT, when you want a structured junior testing path.
- OSCP later, after you can write a report without copying a walkthrough.

The hiring story is still the five CV projects in `docs/CAREER.md`.
