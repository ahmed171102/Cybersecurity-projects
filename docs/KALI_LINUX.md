# Kali Linux: how to use it correctly

A study note for **Ahmed Adel Sayed Goda**, Computer Engineering graduate, Cairo. You are learning SOC work, networks, and ethical hacking for a portfolio. You are not expected to be an expert. Read this file in order. It is meant to stand on its own.

This is professional practice, not an attack cookbook. The only legal places to point testing tools are: a lab you own, a written scope that names the target, or a platform that owns the machine (TryHackMe, Hack The Box, PortSwigger Academy, OverTheWire, picoCTF, VulnHub).

If a tool is mainly used to break into something, this file names it, says what it does, and where a professional is allowed to use it. It does not give the attack steps. Practice those steps on the platforms above.

---

## How to use this file

1. Read sections 1–4 before you install anything.
2. Set up the lab in section 2, then run only the commands in section 3.
3. Use section 5 as a dictionary: look up a tool when you hear the name.
4. Use sections 6–8 when you plan study time or write a portfolio note.

After each major section there is a short “you should be able to say” box. If you cannot say it in your own words, reread that section.

---

## 1. What Kali is and is not

Kali Linux is a Debian-based operating system that comes with a large set of security tools already installed. Offensive Security maintains it. The point of the image is convenience: one virtual machine, many programs, a known layout.

It is a **lab operating system**. Treat it like a workshop, not like a phone or a daily laptop.

| Kali is | Kali is not |
| --- | --- |
| A Debian Linux install with security tools preloaded | Proof that you are a hacker or a SOC analyst |
| A place to learn Linux, packets, and reports | Safer than Ubuntu or Windows by default |
| Useful on an isolated virtual network you control | A daily driver for email, banking, or university work |
| One option among many (a plain Debian or Ubuntu lab also works) | Required for a job. Employers care about method and writing, not the desktop wallpaper |

**Debian-based** means package management looks like Debian: `apt` for updates, the same filesystem layout (`/usr/bin`, `/etc`, `/var/log`), and the same idea of users and permissions. If you already used Ubuntu in college, the shell will feel familiar. The difference is the default toolkit and the default mindset of the tutorials you will find online. Many of those tutorials skip permission and scope. This file does not.

**Why it is a poor daily driver**

- The default tool list includes programs that are easy to misuse.
- Running it as a main OS on your real laptop mixes school work, passwords, and experiment leftovers.
- A broken experiment can break the install. On a virtual machine you roll back a snapshot. On bare metal you may reinstall.
- Some employers and exam rules treat a Kali install on a work device as a policy problem, not a skill.

**Snapshot before you experiment.** A snapshot is a saved picture of the virtual machine’s disk and memory settings. If you install a vulnerable app, change a setting, or fill the disk with captures, you restore the snapshot and get a clean machine back. Take one before the first experiment and name it `clean-start`. Details are in section 2.

**You should be able to say:** Kali is a Debian lab image with security tools. I use it in a virtual machine. I do not use it as my everyday computer. I snapshot before I try something new.

---

## 2. How to set it up correctly

Goal of the lab: two machines that can talk to each other, and that do not sit on your family’s Wi-Fi as extra neighbors.

### What you need

- A Windows (or other) **host** computer with VirtualBox (or another hypervisor you already know).
- Enough disk for two virtual machines. Kali plus one small web app is enough.
- The official Kali virtual image or installer from [kali.org](https://www.kali.org/). Download only from that site. Check the published checksum if the site shows one.
- One **vulnerable application you own**, such as [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) or [DVWA](https://github.com/digininja/DVWA). These are teaching apps. You install them so you have a target you are allowed to test.

You do not need a second physical laptop. You do not need to bridge onto the home router.

### Network mode: host-only, not bridged

VirtualBox can attach a virtual machine to the network in several ways. For practice, use this combination:

| Adapter | Use it for | Do not use it for |
| --- | --- | --- |
| **NAT** (on Kali only, if you want) | `apt` updates and browser access to official docs or legal platforms | Scanning whatever NAT happens to reach |
| **Host-only** | Traffic between Kali, the vulnerable app, and your host | Putting the lab on the same LAN as phones and printers |
| **Bridged** | Almost never for student practice | “So I can see the home network” |

**Host-only** means VirtualBox creates a small private network on the host. The VMs get addresses on that network. They can reach each other. They do not become extra devices on the living-room Wi-Fi.

**Bridged** means the VM asks the home router for an address, like a phone. Your scan or a mis-click then hits the TV, a sibling’s laptop, or a neighbor’s guest network if the router is sloppy. That is how students get into trouble without meaning to.

**Never bridge onto home Wi-Fi for practice.** If a tutorial says “use bridged so nmap can find hosts,” close it. Your lab has one target you installed. You already know its address.

A practical layout:

1. In VirtualBox, open the host-only network settings and keep one host-only adapter.
2. Create a Kali VM. Give it NAT if you need updates, plus the host-only adapter for lab traffic.
3. Create a second VM (Debian or Ubuntu is fine) **or** run Juice Shop / DVWA in a way that listens only on the host-only network. Docker on the host is acceptable if you bind it to the host-only address, not to `0.0.0.0` on a bridged interface.
4. Write down the lab IPs in a text file on the host, for example “Kali `192.168.56.10`, Juice Shop `192.168.56.20`.” Those numbers are examples. Use whatever VirtualBox assigned.
5. Confirm the two VMs can ping each other on the host-only network. Confirm a phone on Wi-Fi cannot reach them.

### Snapshot named `clean-start`

When both VMs boot and the vulnerable app loads in a browser from Kali, shut them down cleanly (or use VirtualBox’s snapshot while running, if you prefer). Take a snapshot of **each** VM. Name it `clean-start`.

Restore `clean-start` when:

- An install filled the disk.
- You changed a setting and cannot undo it.
- You want a known baseline before a new lesson.

Take a second snapshot before a long exercise if you might want to keep that state. Do not let snapshots multiply without names. `clean-start` is the one you always keep.

### Updates and isolation

Use NAT (or a browser on the host) to download updates and documentation. Do the actual testing on the host-only side against the app you own. Do not treat “I can reach the internet from Kali” as “I may scan the internet.”

### If memory is tight

This machine may have little free RAM. Give Kali a modest amount (two gigabytes is a starting point if the host has eight). Close the browser on the host while the VMs run. Do not open three heavy tools at once. A slow, isolated lab is better than a crashed host.

**You should be able to say:** My lab is Kali plus one app I installed, on a host-only network, with a snapshot called `clean-start`. I do not bridge onto home Wi-Fi to practice.

---

## 3. First commands that are safe on your own VM

Open a terminal **inside the Kali virtual machine**. These commands talk to your VM or to the package list. They are not a scan of anyone else.

### Who you are, and whether you are root

```bash
whoami
```

That prints the current username. On current Kali you normally work as a regular user and use `sudo` only when a command needs admin rights. Working as root for every command is a habit from old Kali images. It makes mistakes larger: one typo can change system files.

If `whoami` prints `root`, create a normal user for daily lab work or switch to the default non-root account the image already has. Use `sudo` for updates and for tools that need raw network access.

### Addresses on this VM

```bash
ip a
```

You will see loopback (`127.0.0.1` on `lo`) and one or more Ethernet interfaces (`eth0`, `eth1`). NAT and host-only each get an address. Write them down. Loopback is always “this machine.” The host-only address is how the other VM reaches you.

### Is the TCP/IP stack alive?

```bash
ping 127.0.0.1
```

Stop it with Ctrl+C. Replies mean the local stack works. This does not test the internet and does not test your neighbor.

### Install and update Kali

Use the official repositories after a fresh install or a restored snapshot:

```bash
sudo apt update
sudo apt full-upgrade
```

`update` refreshes the list of packages. `full-upgrade` installs newer versions and may remove a package if that is required to keep the system consistent. Read the list before you confirm. If the host is short on RAM, do this when nothing else heavy is running.

If a package you need is missing:

```bash
sudo apt install <package-name>
```

Replace `<package-name>` with a name you already know you need, such as a documentation package. Do not install random “hacking toolkits” from unofficial sites.

### Where tools live

Most command-line tools are on your `PATH` (often under `/usr/bin`). GUI tools appear in the Kali menu, grouped by purpose (information gathering, web, sniffing, and so on). The menu is a catalog, not a to-do list. You do not need to open every item.

To see whether a program is installed and where it is:

```bash
which nmap
which wireshark
```

`which` prints a path or prints nothing. That is enough for this stage.

### How to read `--help` and `man`

Every serious tool has more flags than you will ever need. Do not collect flag lists from social media. Read the local help first.

```bash
nmap --help
man nmap
```

`--help` is the short list. `man` is the manual page; quit with `q`. You are looking for: what the tool does, what a flag changes, and whether a flag is noisy or destructive. If you do not understand a flag, do not use it.

The same pattern works for other tools you are allowed to run locally (`ip`, `ping`, `apt`).

### Open Wireshark on your own VM

From the Kali menu, open **Wireshark**, or in a terminal:

```bash
wireshark
```

Pick the lab interface (the host-only adapter, or loopback if you only want traffic that stays on this VM). Start a capture. Browse Juice Shop or DVWA from Kali. Stop the capture. Save the file on the VM if you want to study it later.

You are reading **your** packets on **your** virtual network. Do not point the capture at a Wi-Fi monitor interface “to see the building,” and do not take a laptop running Kali to a café to watch other people’s traffic.

### One allowed nmap example (this machine only)

A **connect scan** completes the TCP handshake. It is easy to understand and easy to see in a capture. On your Kali VM:

```bash
nmap -sT -p 1-1024 127.0.0.1
```

That asks: which TCP ports in the first 1024 are accepting connections **on this same machine**? Any other target needs **written scope** (a lab IP you own and wrote down, a contract, or a platform that assigned you that host). Do not add speed flags, script flags, or a second address to “try it.”

If you later scan Juice Shop or DVWA, that is still only allowed because you installed it and it sits on the host-only network you documented. The command above is the one this file is willing to print. Learn the output: open, closed, filtered. Then stop.

**You should be able to say:** I know who I am on the VM, what my addresses are, how to update, how to open a manual, how to open Wireshark on my lab interface, and that nmap on `127.0.0.1` is a lesson, not a hunting license.

---

## 4. The rule for real life

Tools do not create permission. Paper (or a ticket in a company system) does.

A professional test has all of the following. If one is missing, you do not start.

| Piece | What it means in practice |
| --- | --- |
| **Written permission** | A contract, a signed email from someone who owns the system, or a platform’s terms for that room. A verbal “go ahead” from a friend is not enough. |
| **Scope** | Exact hostnames, IP ranges, apps, and accounts you may touch. If it is not listed, it is not yours. |
| **Time window** | Start and end dates (and often hours). Scanning after the window is a new test, and you need a new yes. |
| **Out-of-scope list** | Named systems you must not touch: payment, production databases, a third-party SaaS, a neighbor VLAN. Write it down so you cannot “forget.” |
| **Evidence** | Screenshots, request/response pairs, log lines, timestamps. Enough that a fixer can reproduce the issue. Not a dump of every packet you ever captured. |
| **Report** | What you found, who is affected, how sure you are, what to fix first, and how you tested. Plain language. No movie language. |
| **Retest** | After the owner says it is fixed, you check **that** finding again, in scope, and record pass or fail. |

This is the job. Finding a weakness and not writing it down is not a finished engagement.

### What is out unless a contract names it

- The **public internet** (random IPs, “the whole /8”, shodan-then-scan).
- **School** networks: campus Wi-Fi, the registration portal, a lab you did not get in writing.
- **Employer** networks: the office Wi-Fi, the HR site, a cloud account you can log into for your day job. Access for work is not permission to test.
- Home devices you do not own (a roommate’s phone, a landlord’s router management page).

Egyptian and most other law treats unauthorized access and unauthorized scanning as a crime, not as homework. Portfolio pride is not a defense.

Legal practice that does **not** need a custom contract:

- Your own VMs and the apps you installed.
- TryHackMe, Hack The Box, PortSwigger Academy, OverTheWire, picoCTF, and VulnHub machines, **inside the rules of that platform**. Permission in a room does not move to a university IP.

**You should be able to say:** I can list permission, scope, window, out-of-scope, evidence, report, and retest. Public, school, and work networks are out unless a document names them.

---

## 5. Tool map by job

Read this as a map, not as a shopping list. For each tool: what it is, when a real person uses it, the correct way, the usual mistake, and the harm if you point it at the wrong place.

Offensive tools are named so you recognize them in job posts and write-ups. This file will not walk through the attack. Use TryHackMe, Hack The Box, PortSwigger, OverTheWire, picoCTF, or VulnHub for that practice.

### How jobs line up with tools

| Job | Tools you live in | Tools you only touch with a ticket |
| --- | --- | --- |
| **SOC analyst** | Logs, Wireshark or tcpdump on a capture you were given, `dig`/`nslookup` to understand a name, Suricata/Snort alerts | nmap, Nikto, Burp — only if the playbook and scope say so |
| **Network engineer** | Addressing, firewall policy, `ip` / routing, packet capture on gear you administer | Anything that probes a network you do not run |
| **Application-security tester** | Burp or ZAP on an in-scope app, notes, a report | Metasploit, sqlmap, hydra — only on a scoped pentest or a legal platform, and only when the method matches the rules |

A portfolio that shows a report and a capture is stronger than a portfolio that shows a screenshot of a Kali menu.

---

### nmap

**What it is.** A port and service scanner. It asks hosts which ports accept connections and can guess what is listening.

**When it is used.** A tester maps an **in-scope** range at the start of an engagement so the report lists live hosts and services. A defender may run it against **their own** servers after a change, to see what is exposed. A SOC analyst usually reads nmap output that someone else produced; they do not scan the internet to “hunt.”

**Correct way.** Written scope. The smallest scan that answers the question. Record the command, the time, and the result. The only command this file prints is the localhost connect scan in section 3. Any other address needs that written scope.

**Common mistake.** Scanning a whole university, a cloud region, or “just the home LAN” to learn the flags. Adding aggressive scripts and timing options because a blog did.

**If misused.** You generate noise that looks like an attack. You may hit a third-party host. You can knock over a fragile device. You can also get a disciplinary case or a criminal one.

**Practice:** TryHackMe rooms that teach scanning on **their** machines. OverTheWire does not need nmap for Bandit.

---

### Wireshark

**What it is.** A graphical packet analyzer. You open a live interface or a saved capture (`.pcap` / `.pcapng`) and filter frames.

**When it is used.** SOC: a span port, a tap, or a capture file from an incident. Network engineer: a capture on a router, switch, or firewall **you run**, to see why a flow fails. Tester: a capture on the lab path to understand a request, not to spy on a café.

**Correct way.** Capture only networks you own or were told to capture. On Kali, open Wireshark on the VM and choose the host-only or loopback interface (section 3). Filter to the conversation you care about (`dns`, `tcp.port == 443`, and similar). Write what you saw in plain language: who talked, which ports, whether the payload was encrypted.

**Common mistake.** Promiscuous capture on shared Wi-Fi “to see what people do.” Keeping captures that contain other people’s passwords or cookies. Treating a colorful packet list as a finding without explaining it.

**If misused.** Intercepting other people’s traffic is wiretapping in many places. Captures are evidence and privacy risk. Store them like you would store a disk image: access-controlled, and deleted when the case is closed.

**Practice:** Capture your own Juice Shop or DVWA session. TryHackMe packet rooms. Write a half-page: three facts the capture proves.

---

### tcpdump

**What it is.** A command-line packet capture tool. Same job as Wireshark’s capture engine, without the GUI. Useful on a server that has no desktop.

**When it is used.** Network and SOC staff capture a short window on a host they administer, then copy the file to a workstation to read in Wireshark. Testers use it on a lab VM the same way.

**Correct way.** You have admin rights on that host and a reason. Limit the capture (count, time, or a narrow filter) so you do not fill the disk. You are reading **this** machine’s traffic, not scanning someone else.

**Common mistake.** Leaving a capture running for days. Capturing on a shared interface and publishing the file. Using tcpdump as a substitute for permission to monitor a network you do not run.

**If misused.** Same privacy and legal issues as Wireshark, plus disk-full outages.

**Practice:** Short captures on your Kali VM while you browse the lab app. Open the file in Wireshark and name the protocols.

---

### dig and nslookup

**What they are.** DNS query tools. You ask a resolver for records: A (IPv4), AAAA (IPv6), MX (mail), CNAME (alias), NS (name servers), TXT (text, often used for policy).

**When they are used.** Everyone. SOC: “what does this domain in the alert resolve to?” Network: “did the record change after we edited DNS?” Testers: **passive** recon on names the owner already published, inside scope.

**Correct way.** Query names you have a reason to resolve: your lab, a domain in an alert, or a name in a written scope. Read the answer and the TTL. Notice whether you asked a recursive resolver or an authoritative server.

**Common mistake.** Treating DNS as “hacking.” Sending huge zone-transfer attempts at random companies. Confusing a public record (anyone can ask) with permission to scan the host that the record points to.

**If misused.** A single lookup is normal internet behavior. A campaign of unusual queries plus a scan is what gets you noticed. The bigger error is using a DNS answer as an excuse to attack the IP.

**Practice:** Look up records for a domain you own or a name in a TryHackMe room. Project-style learning: write down record types in your own words.

---

### netstat and ss

**What they are.** Local socket listings. They show which ports **this computer** has open, and which connections are established. `ss` is the modern tool on Linux; `netstat` still appears in older notes.

**When they are used.** You are on a machine you administer (or your lab VM). A service will not start, or you want to confirm a listener is bound to localhost only. SOC and IR use the same idea on a host they are allowed to inspect.

**Correct way.** Run them on **your** VM or on a system in an incident where you have a role. Compare “what should be listening” with “what is listening.”

**Common mistake.** Thinking this scans the network. It does not. The opposite mistake: running a network scanner when all you needed was “is my own web server up.”

**If misused.** Low risk compared with nmap, unless you are on a host you should not be on. Unauthorized login is the real problem in that case.

**Practice:** On Kali, after Juice Shop is running (on either VM), see which ports listen on that machine. Do not turn that into a scan of the host-only range “for fun.”

---

### Nikto

**What it is.** An old, noisy web-server scanner. It requests many known paths and looks for outdated banners, default files, and obvious misconfigurations.

**When it is used.** A tester may run it against an **in-scope** web server to get a first pass of low-hanging issues. A defender may run it against **their** staging site. SOC rarely runs it; they see the log noise it creates.

**Correct way.** Only Juice Shop, DVWA, or a host named in a contract or a legal platform. Expect a long, messy report. Triage: what is real, what is a default-file warning, what is a false positive. Put the real items in a report with evidence.

**Common mistake.** Pointing it at a production site, a university portal, or a live shop because it is “just a scanner.” Believing every line is a critical finding.

**If misused.** It is loud. It can look like an attack in WAF and IDS logs. It can also request URLs that change data on poorly built apps.

**Practice:** Against your lab app only, or a TryHackMe web box. Then write which three items you would actually tell a developer.

---

### Burp Suite

**What it is.** An intercepting web proxy. Your browser sends traffic to Burp; Burp shows the HTTP request and response; you can inspect, repeat, or change a request **in a lab**. PortSwigger makes it. The Community edition is enough to learn.

**When it is used.** This is the daily tool of an application-security tester. SOC may open a saved request if a web alert needs it. Network engineers rarely live here.

**Correct way.** Configure the browser to use the proxy. Install Burp’s CA certificate **in that browser on the lab VM** so you can see HTTPS to your lab app. Work only on Juice Shop, DVWA, PortSwigger Academy, or an app in a written scope. The job is: understand the request, show a weakness with evidence, write a fix. Then turn the proxy off so you do not accidentally send everyday browsing through it.

**Common mistake.** Leaving the proxy on and sending mail or banking through Kali. Using repeater or scanner features on a site that is not in scope. Pasting a full session cookie into a public write-up.

**If misused.** You can change requests that create users, move money, or delete data. On a production site without permission, that is an incident, not a lab.

**Practice:** [PortSwigger Web Security Academy](https://portswigger.net/web-security) in the browser they intend. Then Juice Shop on host-only. Two write-ups in your own words (section 7).

---

### OWASP ZAP

**What it is.** An open-source web proxy and scanner, similar in role to Burp. OWASP maintains it. Good for learning intercept and for a first automated pass on an app **you own**.

**When it is used.** Testers and developers on a staging app they control. Some teams put ZAP in a pipeline against a dedicated test environment.

**Correct way.** Point it at the lab app or a named staging URL in scope. Read every alert. Automated tools duplicate and exaggerate. Your value is triage and a clear report.

**Common mistake.** “ZAP said high, so I am done.” Scanning production. Publishing a raw ZAP HTML dump as a portfolio piece with no explanation.

**If misused.** Same class of harm as Nikto and Burp: noisy requests, possible state change, possible outage.

**Practice:** Same targets as Burp. Compare one finding in ZAP with the same finding shown by hand in the browser. The hand explanation is what you put in a portfolio.

---

### Gobuster and dirb

**What they are.** Programs that try many URL paths (and sometimes hostnames) from a **wordlist** to see which ones exist on a web server. They do not “hack” by themselves. They guess names: `/admin`, `/backup`, and so on.

**What they are used for (name and purpose only).** On a scoped test or a legal platform, a tester checks whether the app left a backup file, a debug page, or an old admin path reachable. A defender uses the same idea as a checklist: those paths should not be on production.

**Correct way.** Only on an app you own or a platform that assigned you the host. The output is a list of paths to inspect and to put in a report if they matter. This file does not give wordlist commands or attack steps.

**Common mistake.** Running a huge wordlist against someone else’s site. Treating every `200` as a critical hole. Ignoring that some sites ban or throttle this traffic.

**If misused.** You generate a high request rate. That can be a denial-of-service and is easy to see in logs. Unauthorized guessing of hidden paths is still unauthorized testing.

**Practice:** TryHackMe and Hack The Box web rooms, or Juice Shop’s own documentation of intended challenges. Learn to **explain** why a leftover path is a problem (backup of source, admin without auth). Do not paste a command line as if that were the skill.

---

### John the Ripper and hashcat (lesson only)

**What they are.** Password-recovery programs. They take a **hash** (and often a salt) and try candidate passwords until the hash matches. John is older and flexible. hashcat is built for heavy use of GPUs.

**The lesson, not the cookbook.**

- A **hash** is a one-way fingerprint. You do not “decrypt” it. You guess inputs until the fingerprint matches.
- A **salt** is extra random data stored with the hash so two users with the same password do not get the same hash. Salts stop simple “one rainbow table for the whole site” shortcuts. They do not make a weak password strong.
- **Slow hashes** (bcrypt, scrypt, Argon2, and similar) are meant to cost time and memory per guess. That is a defensive choice. Fast hashes (unsalted MD5 for passwords) are a design mistake.
- You may only work on hashes **you just created**, hashes from a **legal lab**, or hashes a contract says you may test (for example a password-policy assessment the owner requested).

**When they are used.** A tester demonstrates that a dumped password file from **in-scope** systems is weak, then tells the owner to use a slow hash, unique salts, and a better policy. A defender uses the same tools on **their** test accounts to prove the policy. SOC does not “crack the office” because they are curious.

**Correct way.** Create a hash yourself or use a lab that provides one. Record the **policy lesson**: salt, algorithm, length, rotation, MFA. This file does not include cracking commands and does not tell you to use someone else’s dump.

**Common mistake.** Downloading a leak and “practicing.” That is handling stolen credentials. Another mistake: putting cracked passwords into a public repo.

**If misused.** Credential theft, account takeover, and a very hard conversation with a lawyer.

**Practice:** A lab that generates its own hashes, or a TryHackMe room that issues hashes for that room. Write the defensive paragraph, not a speed-run of flags.

---

### Aircrack-ng suite (policy only)

**What it is.** A set of programs people associate with Wi-Fi assessment: capturing wireless frames, talking about WEP/WPA, and related radio work.

**This file gives no wireless attack steps.** No monitor-mode recipe, no deauth, no evil twin, no WPS attack, no handshake capture walkthrough.

**When a professional touches wireless.** A scoped assessment of a network the **owner** named, with written rules about radios and clients. That is a specialist job. It is not a first-month exercise on a shared apartment access point.

**The defensive lesson (what you should actually do at home and recommend at work):**

- Use **WPA3** if the access point and clients support it. If not, **WPA2 with AES (CCMP)**. Do not use WEP. Do not use WPA-TKIP as the main mode.
- **Turn WPS off.** It is a convenience feature with a long history of weak setups.
- Put printers, cameras, and cheap sensors on a **separate IoT SSID** (or VLAN) that cannot reach your laptop admin ports.
- Change the default router password. Keep the admin interface off the guest network.
- Do not run a second access point that pretends to be the real one. That is an evil twin. Teaching materials that walk through building one are out of scope here.

**Common mistake.** “Practicing” on a neighbor, a café, or a friend’s phone hotspot. Buying an antenna and treating the street as a lab.

**If misused.** Jamming and client-disconnect tricks disrupt service. Impersonating an access point steals sessions. This is both harmful and easy for others to notice.

**Practice:** Configure **your** access point with the policy above. In a course or a legal wireless lab that **owns** the radios, follow **their** workbook. Not this file.

---

### Metasploit (name only)

**What it is.** A framework used in authorized penetration tests and on legal lab platforms to drive known exploit modules, listeners, and post-access tools from one place.

**This file is not a recipe.** No module names to run, no payload generation, no reverse-shell walkthrough, no `msfvenom`.

**When it is used.** A tester on a **scoped** engagement or a Hack The Box / TryHackMe / VulnHub machine, after the rules of that test allow it. The professional moment is: you already know the service and the weakness, you have permission, and you need a controlled way to **show impact** so the report is honest. Then you stop, write the finding, and tell the owner how to patch or mitigate.

**Defensive lesson.** Patch, reduce what is reachable, and monitor. If a lab taught you that an old service falls over, the portfolio sentence is “I would upgrade this service and block the port from the internet,” not “I popped a shell.”

**Common mistake.** Treating Metasploit as the whole skill. Running modules at work “to see.” Generating payloads on a personal laptop and calling that a project.

**If misused.** You are distributing or launching exploit code against a system you do not own. That is the definition of unauthorized access.

**Practice:** TryHackMe and Hack The Box paths that teach the **class of bug** and the **report**. If a room uses Metasploit, stay inside that room.

---

### sqlmap (name only)

**What it is.** An automated tool that tries to find and exploit SQL injection.

**No attack procedure in this file.**

**When it is used.** On a legal platform or a written web-app test that allows automated SQLi tools. Many real engagements **forbid** it on production because it is noisy and can change or lock data.

**Defensive lesson.** Parameterized queries, least-privilege database accounts, and not reflecting raw errors. If sqlmap would have succeeded, the fix is in the application and the database role, not in “blocking the User-Agent.”

**Common mistake.** Pointing it at a school or company login form. Assuming a clean sqlmap run means the app is safe (it does not).

**Practice:** [PortSwigger SQL injection labs](https://portswigger.net/web-security/sql-injection) on their site. Juice Shop’s documented SQLi challenges. Write how the query should have been written.

---

### hydra (name only)

**What it is.** A network logon cracker: many username/password guesses against a service (web forms, SSH, and others).

**No attack procedure in this file.**

**When it is used.** Only when a scoped test or a lab explicitly allows credential guessing, and usually against **test accounts** the owner created. Lockout and account-disable policies exist because this traffic looks like an attack — because it is one.

**Defensive lesson.** MFA, lockout or throttling, no default passwords, and monitoring repeated failures. Do not disable those controls on a real network “so the tool works.”

**Common mistake.** Running it against a friend’s Wi-Fi router, a university VPN, or SSH on the internet.

**If misused.** Account lockouts for real users, and unauthorized access if a guess works.

**Practice:** Rooms on TryHackMe or Hack The Box that teach **authentication** and **lockout**. PortSwigger access-control labs. Explain the control, do not publish a guess list.

---

### Suricata and Snort

**What they are.** Network intrusion detection (and, in some setups, prevention) engines. They inspect packets or flows with **rules** and raise alerts: “this looks like a known exploit pattern,” “this policy forbids that port.”

**When they are used.** SOC and network security. You write or tune rules, reduce false positives, and connect alerts to a ticket. This is the defensive pair to the noisy tools above.

**Correct way.** Run them on traffic you are allowed to see: a lab span, a capture file, or a sensor the organization placed. Start with a clear policy (what is forbidden on this segment). Tune. Measure whether a real lab event would have fired.

**Common mistake.** Dropping a default ruleset on a home PC and declaring you “have an IDS.” Ignoring alerts. Using an IDS as permission to generate attacks on a network you do not own so you can “test the rules.”

**If misused.** Prevention mode can block business traffic. A bad rule is an outage. Generating live attacks to test detection belongs in a **lab** or a scheduled purple-team with a ticket.

**Practice:** Read a small rule, explain it in one paragraph, and match it to a saved lab capture or a sample event. Build the habit: alert → evidence → decide.

---

### Autopsy and Volatility

**What they are.** Forensic tools. **Autopsy** (with The Sleuth Kit underneath) is used on a **disk image** to browse files, timelines, and artifacts in a guided UI. **Volatility** is used on a **memory image** (RAM dump) to list processes, network artifacts, and other volatile state.

**When they are used.** Incident response and digital forensics. The chain of custody matters: where the image came from, who hashed it, who opened it.

**Correct way.** Work on a disk or memory image **you own**, a classroom image, or an image a case owner gave you. Hash the file (SHA-256) before you start. Work on a **copy**. Write what you found with timestamps. You are answering a question (“was this program present?”), not browsing someone’s photos for fun.

**Common mistake.** Imaging a family laptop without a clear case and consent. Analyzing a live work PC with random plugins and overwriting evidence. Publishing personal data from an image.

**If misused.** Privacy harm and spoiled evidence. Forensics without authority is still unauthorized access to data.

**Practice:** Create a small VM, snapshot it, make a disk image of **that** VM, and walk Autopsy on the copy. Classroom memory images for Volatility. Write a one-page case note.

---

### LinPEAS-style enumeration (lab VM only)

**What it is.** Scripts and checklists (LinPEAS, similar “peas” tools, and many blog lists) that collect **local** facts on a Linux machine: users, cron, sudo rights, interesting files, services. The idea is “what could a person who already has a low-privilege shell look at next?”

**This file gives no privilege-escalation procedure.** No exploit chain, no sudo-abuse recipe, no kernel-exploit steps.

**Correct way.** Treat it as a **checklist you understand**, run only on a **lab VM you own** or a legal CTF machine. The skill is knowing why each item matters (world-writable cron, leftover credentials in a file you created for the lab). On a company laptop you were given for work, you do **not** run these scripts to “see what happens.” That can trigger EDR, violate policy, and collect data you have no right to copy.

**Common mistake.** Downloading a script and running it on the office notebook. Pasting the full output into Discord. Thinking the script is a substitute for knowing Linux.

**If misused.** You may exfiltrate secrets, trip security controls, and lose the job you were trying to impress.

**Practice:** On a disposable lab VM, use a **written checklist** (users, listening ports, cron, sudo, file permissions) and fill it in by hand first. If a legal platform later uses an enum script, stay on that VM. The portfolio artifact is the checklist and the hardening note, not a raw dump.

---

### Quick map (print this)

| Tool | Job moment | Correct target | Common mistake |
| --- | --- | --- | --- |
| nmap | Map in-scope hosts | Lab / contract / platform | Scanning campus or the internet |
| Wireshark | Explain a flow | Span, lab, or your capture | Café Wi-Fi snooping |
| tcpdump | Short capture on a box you run | That host | Overnight capture, published pcap |
| dig / nslookup | Understand a name | Alert, lab, in-scope domain | DNS answer used as attack permission |
| netstat / ss | Listeners on **this** host | Your VM or IR host | Confusing it with a network scan |
| Nikto | First-pass web issues | Lab app or scoped URL | Production and “all findings are real” |
| Burp Suite | App test and evidence | Scoped app / Academy | Proxy left on for daily browsing |
| OWASP ZAP | Same, more automation | App you own or staging in scope | Raw scan as the report |
| Gobuster / dirb | Find leftover paths | Lab / platform / scope | Wordlist against strangers |
| John / hashcat | Policy proof on allowed hashes | Hashes you made or a legal lab | Leaked dumps |
| Aircrack-ng suite | Specialist wireless, if ever | Owner’s radios, written rules | Neighbor / café practice |
| Metasploit | Show impact on a allowed lab | Legal lab or pentest scope | Recipe-driven office “test” |
| sqlmap | Automated SQLi where allowed | Platform or scoped web test | School/company login forms |
| hydra | Credential guessing where allowed | Test accounts in scope | Friend’s router, public SSH |
| Suricata / Snort | Detection | Sensor or lab capture | Attacks on real nets to “test IDS” |
| Autopsy / Volatility | Forensics | Image you own or were given | Family/work disk curiosity |
| LinPEAS-style | Local enum checklist | Lab VM / CTF only | Company laptop “enum” |

**You should be able to say:** For any tool in this table I can name the job moment, a legal target, and one mistake. If the tool is offensive, I practice it on a platform, not on Cairo street Wi-Fi.

---

## 6. A day in the life (three roles)

These are ordinary days, not movie days. Notice what people **do not** do.

### SOC analyst

You start with a queue: SIEM alerts, a firewall deny, a user report. You open **logs** first (time, host, user, source IP). You ask whether this is known-good, a misconfiguration, or something to escalate.

If the case needs packets, you open **Wireshark on a span port, a tap, or a lab capture someone stored** — not a scan of the internet, and not nmap against a random cloud IP to “enrich the alert.” You may use `dig` on a domain that appeared in the alert. You write a timeline. You pass a clean summary to the next person.

Kali is optional. Many SOC stations are Windows or a plain Linux jumphost with a browser to the SIEM. If you use Kali, it is to read a pcap or to match a protocol, still inside the case.

**Portfolio version of this day:** a short case note from a sample log or a pcap you captured in the lab. Question, evidence, decision.

### Network engineer

You own addressing and reachability. You change a **subnet**, a VLAN, or a **firewall** rule because an application owner asked, with a ticket. You verify with ping and with a capture **on the gear you administer** (or on a span that the design already has). You do not run a discovery sweep of a building you do not run.

Kali can be a convenient box with `ip`, Wireshark, and `dig`. It is not required. Breaking a routing table and fixing it on a lab topology teaches more than collecting scanner screenshots.

**Portfolio version of this day:** a diagram of your host-only lab, the addresses, and one firewall rule you can explain (what it allows, what it denies, why).

### Application-security tester

You read the **written scope** in the morning: URLs, accounts, what is forbidden (no denial-of-service, no real customer data). You run **Burp** (or ZAP) against **that** app. You try to understand how authentication and access control work. You collect one request/response pair per finding. You write the **report** in the afternoon: impact in business language, steps to reproduce, fix, residual risk. You schedule a **retest** when they say they patched.

You do not start the day with Metasploit. You do not sqlmap a production checkout flow because it is faster. If the contract allows a specific automated tool, you still triage.

**Portfolio version of this day:** two findings against Juice Shop or PortSwigger Academy, in your words, with a fix. Look like a tester, not like a tool screenshot.

**You should be able to say:** SOC lives in logs and allowed captures. Network lives in design and gear you run. Appsec lives in Burp-plus-report on a named app. None of them scan the public internet for practice.

---

## 7. What to practice the first month

Keep the lab small. Write more than you collect.

| Order | What | Why |
| --- | --- | --- |
| 1 | [TryHackMe](https://tryhackme.com/) beginner path | Guided, legal machines, Linux and network vocabulary |
| 2 | [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) levels 0–15 | Files, permissions, SSH, reading error messages — no Kali required |
| 3 | [PortSwigger](https://portswigger.net/web-security) labs: SQL injection, XSS, access control, **on their site** | This is real appsec practice with a proxy, in a place that owns the app |
| 4 | Two write-ups **in your own words** | Portfolio evidence. What was in scope, what you saw, what you would fix |

Rules for the write-ups:

- Do not paste a public walkthrough.
- Name the platform and the room or lab.
- Include permission in one sentence (“PortSwigger Academy lab,” “TryHackMe room X”).
- Include at least one piece of evidence you produced (a redacted response, a screenshot of **your** session, a log line).
- Include a fix a developer could apply.

Optional later, still legal: Hack The Box starting machines, picoCTF, a VulnHub VM on host-only. Same report habit.

What **not** to spend the first month on: wireless attack blogs, Metasploit payload posts, cracking leaked dumps, or “scan your neighborhood.”

**You should be able to say:** After a month I have beginner rooms, Bandit 0–15, three PortSwigger topics, and two reports I wrote myself.

---

## 8. Do not do this

Short list. If you catch yourself doing one of these, stop and restore `clean-start` if you need a clean head.

1. **Scanning the internet** — random IPs, cloud ranges, “just this /24 I found.” That is not a lab.
2. **Running tools on a friend’s Wi-Fi** — or a café, a campus SSID, a shop. Friendship is not a contract. The router is not yours.
3. **Disabling the host firewall to “see what happens”** — you open the host to whatever the VMs and the LAN can do. Learn by adding a **specific** allow rule in the lab, then putting the firewall back. Curiosity is not a reason to drop the shield on the computer that holds your mail.
4. **Committing VPN private keys** — or any key, password, Burp CA, or `.pcap` with session cookies — to GitHub. Use a sample config with placeholders. Rotate anything that already leaked.
5. **Treating Kali as proof of skill without a report** — a screenshot of a tool menu does not show that you can scope, explain, or fix. The report is the skill.

Also do not: install Kali as the only OS on a machine you need for life; bridge the lab onto home Wi-Fi; run LinPEAS on a company laptop; keep captures of other people; follow a blog that skips permission.

**You should be able to say:** I can list those five mistakes and why each one is a problem.

---

## Check yourself

Close the file and answer out loud.

1. Why is Kali a lab OS and not a daily driver?
2. What network mode do you use for the vulnerable app, and why not bridged?
3. What is the snapshot called, and when do you restore it?
4. Recite the seven pieces of a real engagement (section 4).
5. Which nmap command is printed in this file, and what must exist before any other target?
6. Name one SOC tool, one network habit, and one appsec tool from section 6.
7. What are the four first-month practices?
8. Give one defensive sentence each for wireless, passwords (salts / slow hashes), and SQL injection — without describing an attack.

If a question fails, go back to that section. You do not need more tools. You need the rule and the report.

---

## Where this sits with the rest of the repo

This note is the Kali and professional-tool layer. Other docs in this folder cover concepts, how the projects fit, and career direction. The ethical rule is the same everywhere: lab you own, written scope, or a platform that owns the target.

Official starting points:

- [Kali documentation](https://www.kali.org/docs/)
- [TryHackMe](https://tryhackme.com/)
- [Hack The Box](https://www.hackthebox.com/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [OverTheWire](https://overthewire.org/wargames/)
- [picoCTF](https://picoctf.org/)
- [VulnHub](https://www.vulnhub.com/)
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)
