# 35 — Secure DevOps

## What this is

`security_gate.py` fails if another `.py` file in this folder assigns a hard-coded secret. `app_demo.py` only prints `demo app ok`. A sample GitHub Actions workflow runs the gate.

## Why it matters

A secret in source is copied forever. The gate is a cheap check before the build is called green.

## How to run

```bash
python3 projects/35-secure-devops/security_gate.py
python3 projects/35-secure-devops/app_demo.py
```

## Portfolio deliverable

The green gate output, plus a screenshot of a failing run after you temporarily add `SECRET = "oops"` to a copy of the demo. This is a CV project.

## Exercise

Add `PASSWORD = "lab"` to a throwaway file in this folder, run the gate (it should fail), then delete the file and confirm `no hard-coded secret assignment` comes back.
