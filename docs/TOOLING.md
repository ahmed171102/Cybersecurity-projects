# Tooling

Use these on a lab virtual machine, or on a site that gave you the target. Do not point them at your university, an employer, or the public internet. A Kali-specific map is in `docs/KALI_LINUX.md`.

| Tool | What you use it for | Where it shows up here |
| --- | --- | --- |
| `dig` | DNS answers, close to project 04 | Lab VM |
| `nmap` | Which ports are open | Project 06 is a small connect-scan you can read. Nmap belongs on the lab VM |
| Nikto | Obvious web-server issues | Only against Juice Shop or DVWA on your lab |
| Burp Suite | Inspect and repeat your own browser traffic to a lab app | PortSwigger Academy and local Juice Shop |
| OWASP ZAP | A scanner for a web app you own | The lab VM, then triage with project 40 |
| Wireshark | Read packets | Project 02’s worksheet. Capture only networks you own |
| Suricata | Network detection rules | Project 28 is the idea, on sample events, not a live attack |

Practice sites, again: TryHackMe, Hack The Box, picoCTF, PortSwigger Web Security Academy, OverTheWire, VulnHub.

Wireshark display filters worth memorizing after project 02:

- `dns`
- `tcp.port == 443`
- `tcp.flags.syn == 1`

tcpdump on the lab VM, ten packets, then stop:

```bash
sudo tcpdump -i any -c 10 -n
```

That reads your own traffic. It is not a scan of someone else.
