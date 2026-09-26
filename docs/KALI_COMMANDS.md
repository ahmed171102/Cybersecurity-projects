# Kali and Linux commands for Ahmed Adel Sayed Goda

This is a study sheet for everyday Linux shell work and the Kali tools a junior SOC / networks / ethical-hacking student should recognize.

Use these commands on **your own Kali lab VM** or as a local administrator on a machine you own. Do not point scanners or Kali tools at the public internet, a workplace, a school, or anyone else's network.

Legal lab only means: a VM you built, a classroom range you were given in writing, or a target that is listed in a written scope.

---

## 1. How a command is shaped

A command is usually three pieces:

| Piece | What it is | Example |
| --- | --- | --- |
| Program | The tool you run | `ls` |
| Flags | Switches that change behavior | `-l` or `--help` |
| Arguments | The thing the program works on | a path, a host, a filename |

Example:

```bash
ls -l /home
```

- `ls` is the program
- `-l` is a flag (long listing)
- `/home` is the argument (which folder)

You can combine short flags: `ls -la` is the same idea as `ls -l -a`.

**Stop a running command:** press `Ctrl+C`. The process should quit. If a program is waiting for you to type, `Ctrl+C` is still the first thing to try.

**Read help before you guess:**

```bash
ls --help
man ls
```

`--help` is a short reminder. `man` (manual) is the longer page. Press `q` to leave `man`. If `man` is missing a page, try `whatis ls` or search the tool name plus "man page".

You do not need to memorize every flag. You need to know how to ask the program what it does.

---

## 2. Identity and files

These are the commands you will use every day. They work the same on Kali and on a normal Linux shell.

### Who you are

```bash
whoami
id
```

`whoami` prints your username. `id` prints your user id, group id, and groups. In a SOC lab this answers "which account am I holding right now?"

**sudo vs root.** `root` is the full administrator account. `sudo` means "run this one command with administrator rights," usually after your password. Prefer `sudo` for one task. Do not stay logged in as root for browsing, editing notes, or installing random tools.

```bash
sudo whoami
```

That should print `root` if sudo is set up. You still are not "living as root." You ran one command as root.

### Where you are and what is here

```bash
pwd
ls
ls -la
cd
cd /tmp
cd ~
cd ..
```

| Command | Job |
| --- | --- |
| `pwd` | Print the folder you are in |
| `ls` | List names in this folder |
| `ls -la` | Long list, including hidden files (names that start with `.`) |
| `cd` | Go to your home folder |
| `cd /tmp` | Go to that path |
| `cd ~` | Home folder |
| `cd ..` | One folder up |

### Create, copy, move, delete

```bash
mkdir lab-notes
cp notes.txt lab-notes/
mv notes.txt lab-notes/old-notes.txt
```

`mkdir` makes a folder. `cp` copies. `mv` moves or renames.

```bash
rm lab-notes/old-notes.txt
```

**`rm` is permanent.** Linux does not put the file in a Recycle Bin. There is no undo. Do not run `rm -r` on a path until you have read the path twice. Never practice `rm` on `/` or `$HOME` as a joke.

### Read files

```bash
cat notes.txt
less notes.txt
head -n 20 notes.txt
tail -n 20 notes.txt
```

| Command | Job |
| --- | --- |
| `cat` | Dump the whole file to the screen. Fine for short files. |
| `less` | Page through a long file. Arrow keys to move. `q` to quit. |
| `head` | First lines. `-n 20` means twenty lines. |
| `tail` | Last lines. Useful for logs. |

### Find text and files

```bash
grep "Failed" /var/log/auth.log
find . -name "*.txt"
```

`grep` searches **inside** files for a string. `find` searches **for** files by name or type, starting from a folder (`.` means "here").

If `auth.log` is missing on your Kali build, use `journalctl` in the log section below. Distros store auth lines in different places.

### Permissions at a basic level

```bash
ls -l notes.txt
chmod 644 notes.txt
```

`ls -l` shows permissions on the left (`rw-r--r--` and similar). `chmod` changes them.

A simple mental model:

- `644` — you can read and write; others can read
- `755` — you can run a folder or a script; others can enter/read but not write

You do not need octal memorized on day one. You do need to know that a world-writable file (`777`) is usually a mistake on a shared or lab host.

---

## 3. Network on your own machine

These commands describe **this computer**. They are how you check "am I on the network, and what ports are listening here?"

```bash
ip a
ip r
ping -c 4 127.0.0.1
ss -tulpn
```

| Command | Job |
| --- | --- |
| `ip a` | Addresses and interfaces (old cousin: `ifconfig`) |
| `ip r` | Routes. Default route is how you leave this machine. |
| `ping -c 4 127.0.0.1` | Four pings to yourself. Proves the stack is up. `-c` stops it so it does not run forever. |
| `ss -tulpn` | Listening TCP/UDP sockets and which process owns them |

`127.0.0.1` is this machine. It is the safe first target for ping and for the nmap example later.

```bash
tracepath 127.0.0.1
# or, if installed:
traceroute 127.0.0.1
```

`traceroute` / `tracepath` show hops toward a host. On your laptop, start with localhost. For any other host, the destination must already be in a written lab scope.

```bash
dig example.com
getent hosts example.com
```

`dig` asks DNS and shows the answer plus the server that answered. `getent hosts` asks the same name-resolution path the system uses (hosts file, then DNS, depending on setup). Use a name you are allowed to query. Looking up a public name you already type in a browser is normal. Scanning random ranges is not.

### Windows cousins

Your daily PC is Windows. Same questions, different names.

| Question | Linux (Kali / normal shell) | Windows |
| --- | --- | --- |
| My addresses | `ip a` | `ipconfig` / `ipconfig /all` |
| Listening ports | `ss -tulpn` | `netstat -ano` or PowerShell `Get-NetTCPConnection` |
| DNS lookup | `dig` or `getent hosts` | `nslookup` |
| Ping myself | `ping -c 4 127.0.0.1` | `ping 127.0.0.1` (Ctrl+C to stop if it loops) |

---

## 4. Packages and the system

Kali and Debian-family systems use `apt`.

```bash
sudo apt update
```

`update` refreshes the **list** of available packages. It does not upgrade software yet.

```bash
sudo apt upgrade
```

`upgrade` installs newer versions of packages you already have.

**Do not upgrade blindly on a daily laptop** (or a VM you need tomorrow). An upgrade can change a driver, break a lab snapshot, or restart services. On a throwaway Kali lab VM, upgrades are normal after a snapshot. On a machine you use for school, work, or notes, read what apt is about to change, or upgrade when you have time to fix a surprise.

**Snapshot the VM first.** In VirtualBox, VMware, or Hyper-V, take a snapshot before `apt upgrade` or before installing extra Kali metapackages. If the upgrade goes badly, you roll back. That is cheaper than reinstalling.

```bash
uname -a
systemctl status ssh
journalctl -u ssh -n 50
```

| Command | Job |
| --- | --- |
| `uname -a` | Kernel and machine string. Useful when a guide says "this is for this kernel." |
| `systemctl status ssh` | Is the SSH service loaded, running, or failed? Service name may be `ssh` or `sshd`. |
| `journalctl -u ssh -n 50` | Last 50 journal lines for that service |

`systemctl` talks to systemd. `status` is read-only and safe. Do not enable random internet-facing services on a VM that is bridged to your home LAN unless you know why.

---

## 5. Logs

SOC work is often "read what already happened."

```bash
tail -f /var/log/auth.log
```

`tail -f` follows a file as new lines arrive. Stop with `Ctrl+C`. If the file does not exist, skip to `journalctl`.

```bash
grep Failed /var/log/auth.log
```

That is a local search for the word `Failed` in the auth log on **this** machine. It is how you notice failed logins on your own lab VM.

```bash
journalctl -u ssh --since "1 hour ago"
```

Same idea through systemd: SSH service logs from the last hour. Change `ssh` if your unit name is `sshd`. This is your box, your hour, your service.

---

## 6. Hashes and files

```bash
sha256sum notes.txt
file notes.txt
```

`sha256sum` prints a fingerprint of the file bytes. If the hash changes, the file changed. Use this on installers you downloaded, on evidence you own, or on a file you just created.

`file` guesses the real type (text, ELF binary, image) from content, not from the extension. A renamed `.txt` that is actually a binary will show up here.

---

## 7. Kali tools a junior should recognize

The table is recognition, not a cookbook. **Name-only** rows mean: know the job, do not run an attack command from this file. Where a command is shown, it is for your lab VM or `127.0.0.1` only.

| Name | One-sentence job | Correct real-life use | Common mistake |
| --- | --- | --- | --- |
| nmap | Maps ports and services on a host you are allowed to test. | Written scope, lab VM, or localhost. Example only: `nmap -sT -p 1-1024 127.0.0.1`. | Scanning the internet, a neighbor, or a company "to see what happens." Do not add aggressive NSE scripts. |
| wireshark | GUI packet capture and protocol view. | Capture on your lab VM interface, or open a pcap you are allowed to have. | Capturing on a shared/work network without permission. |
| tshark / tcpdump | Text packet capture. Same idea as Wireshark, no GUI. | On the lab VM: `tcpdump -i any -c 10 -n` (ten packets, no DNS lookups). `tshark` is the Wireshark CLI if installed. | Leaving a capture running on a busy interface until the disk fills. |
| dig | DNS lookup with detail. | Resolve names you are allowed to query. See section 3. | Using DNS tools as a cover for scanning networks you do not own. |
| nikto | Old web-server checklist scanner. | Only a web app in your lab or in a written scope. | Pointing it at a live site you found in a browser. No attack walkthrough here. |
| burpsuite | Intercepting web proxy for HTTP you send yourself. | Your lab app, browser pointed at Burp, scope set to that app. | Leaving "intercept all" on and browsing your bank or university portal through it. |
| zaproxy | OWASP ZAP. Similar job to Burp: proxy and lab web testing. | Same rule: your app or written scope. | Automated spider/scan against a site that is not yours. |
| netdiscover | Passive/active host discovery on a **lab LAN**. | Name only in this sheet. Use it only on a virtual network you created. | Running discovery on a cafe, dorm, or office LAN. No command here. |
| gobuster | Directory/vhost wordlist requester against a web server. | Name only. Legal lab web target only. | Wordlist blasting random websites. No command here. |
| sqlmap | Automated SQL injection tester. | Name only. Legal lab only. | No attack command in this file. Do not run it against anything that is not in scope. |
| hydra | Online password guesser against login services. | Name only. Legal lab only. | No attack command in this file. Guessing real accounts is a crime. |
| john / hashcat | Offline password-hash recovery. | Lesson: a **salt** makes each hash unique; a **slow hash** (bcrypt and similar) is meant to be expensive. Only hashes **you created** or a **legal lab** hash set. | No attack procedure here. Do not take hashes from a system you do not own. |
| aircrack-ng | Wi-Fi assessment suite. | Policy only: your **own** access point, or a classroom AP you were told to use. | No deauth, no capture recipe, no crack command in this file. Other people's Wi-Fi is off limits. |
| metasploit | Exploit framework. | Name only. Legal lab only. | No payloads, no msfvenom, no reverse shells in this file. |
| suricata | Network detection / IDS engine. | Detection: alerts on traffic you are allowed to inspect (lab tap, your VM). | Treating alerts as proof of guilt without checking the packet and the host. |
| autopsy | GUI for disk forensics. | A **disk image you own** or were given as evidence in a class. | Opening someone else's drive "out of curiosity." |

---

## 8. First hour on a new Kali VM

Do this in order on **your** new VM. Snapshot first if the hypervisor lets you.

1. Log in as your normal user, not as a habit of using root for everything.
2. `whoami` then `id` — confirm the account.
3. `pwd` then `ls -la` — see home and hidden files.
4. `uname -a` — know the kernel string.
5. `ip a` then `ip r` — see interfaces and the default route.
6. `ping -c 4 127.0.0.1` — stack is alive.
7. `ss -tulpn` — what is listening on this VM.
8. `dig example.com` or `getent hosts example.com` — DNS path works (or you see why it does not).
9. `sudo apt update` — refresh package lists. Stop before upgrade if you have not snapshotted.
10. Take a VM snapshot. Then, if you want updates: `sudo apt upgrade` and read the prompt.
11. `systemctl status ssh` — know whether SSH is even installed/running.
12. `journalctl -u ssh --since "1 hour ago"` — if the unit exists; otherwise skip.
13. `mkdir -p ~/lab-notes` and write one sentence about what this VM is for.
14. `sha256sum` on a file you create in `~/lab-notes` so you have done a hash once.
15. `file` on that same file.
16. Optional, still localhost only: `nmap -sT -p 1-1024 127.0.0.1`
17. Optional, on this VM only: `tcpdump -i any -c 10 -n` then `Ctrl+C` if it waits.
18. Stop. Do not install extra attack metapackages until you have a written lab goal.

---

## 9. Do not run this on the internet

- Do not scan, spider, brute-force, or "just test" hosts that are not in a **written scope**.
- `127.0.0.1` and your own lab VMs are the default classroom. Anything else needs permission in writing.
- Kali is a toolbox. Owning the ISO is not permission to use the sharp tools.
- Workplace, university, cafe, and neighbor networks are not labs.
- If a command would send probes, guesses, exploits, or wireless attacks toward a third party, do not run it. This file will not give you those commands.
- When you are unsure, do not run it. Ask a supervisor or use a isolated VM network with no bridge to the house LAN.

Study the help text, the logs on your own box, and the safe examples above. That is enough for the first months of SOC, networks, and ethical hacking.
