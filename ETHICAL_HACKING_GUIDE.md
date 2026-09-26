# Ethical hacking guide

Test only where you have written permission. A lab you installed, a platform that owns the target, or a contract that names the hosts and the dates. A friend saying "try my site" in chat is not permission.

This repo does not include exploit payloads, malware, or a real phishing site. Project 42 only cracks hashes it just created. Project 06 only connects to loopback or private addresses.

## Legal places to practice

- [TryHackMe](https://tryhackme.com/)
- [Hack The Box](https://www.hackthebox.com/)
- [picoCTF](https://picoctf.org/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [OverTheWire](https://overthewire.org/wargames/)
- [VulnHub](https://www.vulnhub.com/)

Permission in a room applies to that room. It does not transfer to your university, your employer, or a random IP.

## Phases

1. **Recon** — names, DNS, and what the owner already published. Project 39 does passive DNS.
2. **Scan** — which services are open, on hosts that are in scope. Project 06 is the local version.
3. **Access** — on a legal lab, show how a weakness opens a door. In this repo, study the class of bug (project 41) and the fix (projects 31 and 49).
4. **Post-access** — on a legal lab, see how far the door goes. Project 43 lists checks for a VM you own. Project 44 names Active Directory techniques and one defense each.
5. **Report** — evidence, impact, fix, retest. Project 50.
6. **Detection** — what a defender would have seen. Project 52.

## Lab

1. Install VirtualBox.
2. Create an isolated host-only network. Do not bridge it onto your home Wi-Fi.
3. Install Kali on that network if you want the usual tools.
4. Install OWASP Juice Shop or DVWA as the only web target.
5. Take a snapshot before each exercise.

Capture traffic and run scanners only on that network.

## First month

1. TryHackMe’s beginner path.
2. OverTheWire Bandit, levels 0–15.
3. PortSwigger labs for SQL injection, XSS, and access control. Do them on the Academy site.
4. Write two short reports in your own words: what you were allowed to touch, what you observed, and what you would fix. Use `projects/50-pentest-report-engagement` as the shape. Do not paste a public write-up.
