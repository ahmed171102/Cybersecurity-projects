# 23 — Zero-trust API

## What this is

A Flask API on `127.0.0.1:5001`. `POST /login` returns a 5-minute HS256 JWT. `alice` / `alicepass` is an admin. `bob` / `bobpass` is a user. `GET /me` and `GET /reports` accept either role. `GET /admin/stats` is admin only. The signing secret is the `JWT_SECRET` environment variable. The default is a lab string.

## Why it matters

A token that expires, and a role check on the route, is the smallest version of "do not trust the caller just because they reached the port."

## How to run

```bash
python3 projects/23-zerotrust-api/app.py
```

Change `JWT_SECRET` outside a lab. These passwords exist only so the demo can log in.

```bash
curl -s http://127.0.0.1:5001/login -H "Content-Type: application/json" -d "{\"username\":\"alice\",\"password\":\"alicepass\"}"
```

Send the token back as `Authorization: Bearer ...`.

## Portfolio deliverable

Show alice opening `/admin/stats` and bob receiving 403 on the same path. This is a CV project. See `docs/CAREER.md`.

## Exercise

Call `/login` five times with a wrong password, then once with the real password. You should get 429. Restart the process to unlock. Then call `/health` with no token. It should stay 200.
