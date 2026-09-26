# 49 — API security lab

## What this is

Flask on `127.0.0.1:5005`. Accounts: alice, bob, carol. Header `X-User` defaults to alice.

- `GET /account/<id>` returns any account. That is the bug (insecure direct object reference).
- `GET /secure/account/<id>` returns 403 if the owner is not the caller.

`test_idor.py` prints both results. Start the API, then run the test. If the API is not up, the test uses Flask's in-process client so you can still see the numbers.

## Why it matters

A hidden URL is not access control. The server has to compare the caller with the record.

## How to run

```bash
python3 projects/49-api-security-lab/vulnerable_api.py
```

In a second terminal, from this folder so the import works:

```bash
cd projects/49-api-security-lab
python3 test_idor.py
```

Or from the repo root, after `export PYTHONPATH=$(pwd):projects/49-api-security-lab`.

## Portfolio deliverable

The three status codes: 200 on the broken route, 403 on the secure route for bob, 200 for alice reading alice. This is a CV project.

## Resume line

Showed an API that returned any account by id, then added an owner check that returns 403 for the same request.

## Exercise

Add `GET /secure/accounts` that lists only the caller's record. Confirm alice never sees bob's email.
