# Career notes

Ahmed Adel Sayed Goda, Cairo. Computer Engineering, AASTMT, 2021–2026. Backend and AI internship work on secure REST APIs, rate limiting, and encryption. Network internship work on Cisco firewalls, Wireshark, and Nmap.

Target roles: application security, and securing AI or backend systems. The portfolio should sound like that. A list of 52 folder names does not.

Show these five, in this order: 31, 49, 23, 35, 32. Leave the rest as practice you can talk about if asked. Copy-paste resume lines and the one-page draft are in `docs/CV_AND_PORTFOLIO.md`.

## Project 23 — zero-trust API

Built a small Flask API that issues a 5-minute JWT and separates admin routes from user routes. Lab accounts are local and documented. The signing secret comes from the environment.

CV bullet: Issued short-lived JWTs for a lab API and enforced role checks so a normal user cannot read admin stats.

## Project 31 — secure notes app

SQLite notes app with Werkzeug password hashes, a CSRF field, and parameterized queries. This is the closest project to the API internship.

CV bullet: Built a notes service that stores password hashes, rejects cross-site form posts, and sends SQL values as parameters instead of pasted strings.

## Project 49 — API object check

`GET /account/<id>` returns any account. `GET /secure/account/<id>` returns 403 when the caller is not the owner. `test_idor.py` prints both.

CV bullet: Reproduced an insecure direct object reference in a lab API and added an owner check that returns 403 for the same request.

## Project 32 — threat model

STRIDE table and a data-flow diagram for project 31.

CV bullet: Wrote a STRIDE model for the notes app, tying spoofing, tampering, and elevation to the login, CSRF, and role controls already in the code.

## Project 35 — security gate

`security_gate.py` fails if another Python file in that folder assigns a secret in source. A sample GitHub Actions workflow runs it.

CV bullet: Added a CI gate that fails the build when a Python file hard-codes a secret assignment.

## How to talk about the network internship

Pair it with projects 02, 05, 06, and 17. One sentence is enough: you can read a subnet, a handshake, and a firewall rule, and you practiced that on Cisco gear and in these labs. Do not claim a production SOC you did not work in.
