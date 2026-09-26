# 43 — Privilege escalation lab

## What this is

`privesc_checklist.py linux|windows` prints enumeration commands: `sudo -l`, SUID, cron, `systeminfo`, services, `whoami /priv`.

## Why it matters

On a VM you own, you need a list of what to look at after you already have a normal login. That list is not an exploit.

## How to run

```bash
python3 projects/43-privilege-escalation-lab/privesc_checklist.py linux
```

Run the printed commands only inside a lab VM you installed.

## Portfolio deliverable

The output of `sudo -l` from that VM, with one sentence on whether any command may run as root.

## Exercise

Run the linux list, then windows. On a VM you own, run sudo -l and paste the output into a note.

