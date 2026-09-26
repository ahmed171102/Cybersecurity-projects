# CV, resume, and portfolio

Ahmed Adel Sayed Goda. Cairo. Computer Engineering, AASTMT, 2021–2026. Target: application security, and securing AI or backend systems.

Put **five** projects on the resume. Pin the same five on GitHub. Do not list all 52. The other labs are practice if an interviewer asks how you learned networks or logs.

Repo: https://github.com/ahmed171102/Cybersecurity-projects

## What goes where

| Place | How many | Which |
| --- | --- | --- |
| Resume / CV, Projects | 5 lines | 31, 49, 23, 35, 32, in that order |
| GitHub pinned repos or the README table | The same 5 | Link each folder |
| Portfolio page, if you add a sixth tile | Optional | 27 mini SIEM, or 17 firewall simulator |
| Do not put on the resume | The rest | 01–22, 24–30, 33, 34, 36–48, 50–52 |

Order on the resume is the order a hiring manager cares about: an app you built, a bug you fixed, tokens and roles, a pipeline check, then the threat model that explains the app.

## Resume lines (copy these)

**Secure notes app** — `projects/31-secure-webapp`  
Built a notes app that stores password hashes, blocks forged form posts with a CSRF field, and sends SQL values as parameters.

**API access control** — `projects/49-api-security-lab`  
Showed an API that returned any account by id, then added an owner check that returns 403 for the same request.

**Token API** — `projects/23-zerotrust-api`  
Built a lab API that issues 5-minute JWTs and returns 403 when a normal user calls an admin route.

**Secret scan in CI** — `projects/35-secure-devops`  
Added a build check that fails when a Python file assigns a secret in source.

**Threat model** — `projects/32-threat-model`  
Wrote a STRIDE model for that notes app and tied each threat to a control already in the code.

## One-page resume draft

Replace the bracketed internship lines with the real employer, dates, and city. Do not invent a company name or a metric you did not measure.

```text
AHMED ADEL SAYED GODA
Cairo, Egypt
GitHub: github.com/ahmed171102
[phone] · [email]

APPLICATION SECURITY / SECURE BACKENDS

Computer engineering graduate. Internship work on secure REST APIs
(authentication, rate limiting, encryption) and on Cisco firewalls,
Wireshark, and Nmap. Portfolio shows the same skills in small labs:
hashed passwords, short-lived tokens, and an access-control fix.

EDUCATION
B.Sc. Computer Engineering, AASTMT, Cairo, 2021–2026

EXPERIENCE
Backend / AI intern — [employer, dates, city]
- Worked on secure REST APIs, rate limiting, and encryption.
- [One task you actually did, in your own words.]

Network intern — [employer, dates, city]
- Worked with Cisco firewalls, Wireshark, and Nmap on networks in scope.
- [One task you actually did, in your own words.]

PROJECTS
Secure notes app — github.com/ahmed171102/Cybersecurity-projects
- Stores password hashes, checks a CSRF field, and uses parameterized SQL.

API access control (same repo, project 49)
- Reproduced an insecure direct object reference and returned 403
  when the caller did not own the account.

Token API (project 23)
- Issues 5-minute JWTs and blocks a normal user from admin stats.

Secret scan (project 35)
- Fails a build when a Python file hard-codes a secret.

Threat model (project 32)
- STRIDE for the notes app, mapped to the controls above.

SKILLS
Python, Flask, REST, JWT, SQL, password hashing, CSRF
Networks: subnets, firewalls, packet capture (Wireshark)
Labs: Linux, VirtualBox. Security+ / eJPT: not yet — do not list them.
```

## What to demo in five minutes

1. Project 49: broken route returns bob's account to alice; secure route returns 403.
2. Project 23: alice gets admin stats; bob gets 403.
3. Project 31: log in as `demo`, save a note, point at the hash and the CSRF field in the form.
4. If they ask "how did you decide what to build?": open the STRIDE table in project 32.
5. If they ask about pipelines: run project 35 and show the passing line.

## What not to claim

- A production SOC, a penetration test for a paying client, or a cybersecurity master's.
- All 52 projects, Kali as a skill by itself, or a certificate you have not passed.
- Numbers you did not measure ("reduced risk by 40%").

The network internship is one sentence plus projects 05 and 17 if they ask about firewalls. It is not the headline. The headline is the API work.
