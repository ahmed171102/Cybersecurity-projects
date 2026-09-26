# 18 — Linux hardening

## What this is

A checklist and a read-only script. It prints the user, whether you are root, and whether `ufw`, `ssh`, and an sshd config are visible. It does not change the machine.

## Why it matters

Hardening is a list you can re-check. A script that only reads is safe to run while you are still learning.

## How to run

```bash
python3 projects/18-linux-hardening/harden_check.py
```

On Windows many lines will say the Linux tools are missing. That is expected. Run it again inside the Ubuntu VM.

## Portfolio deliverable

The script output from the VM next to a checked copy of `CHECKLIST.md`.

## Exercise

Run harden_check.py on Windows (tools missing is fine) and again on the Ubuntu VM. Check two boxes on CHECKLIST.md from the VM output.

