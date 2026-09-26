# 31 — Secure web app

## What this is

A Flask notes app on `127.0.0.1:5002`. Passwords are stored with Werkzeug's hash. The note form has a hidden CSRF field. SQL uses `?` placeholders. The demo user `demo` / `demo-pass-123` is created if it is missing.

## Why it matters

This is the same shape as a small backend: identity, a form, and a database. The three controls are the ones reviews look for first.

## How to run

```bash
python3 projects/31-secure-webapp/app.py
```

Open http://127.0.0.1:5002/login and sign in as `demo`.

## Portfolio deliverable

A note saved in the app, plus a sentence each on the hash, the CSRF field, and the placeholder. This is a CV project. See `docs/CAREER.md`.

## Exercise

Paste a note longer than 500 characters. The app should refuse it. That is the denial-of-service row from project 32. Then save a short note and confirm it still appears.
