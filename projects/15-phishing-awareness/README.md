# 15 — Phishing awareness

## What this is

A static quiz. Message A is an urgent lookalike link. Message B tells you to open the official app. There is no password form.

## Why it matters

Most account theft starts with a message, not with a clever program. The habit is: do not use the link, open the app you already have.

## How to run

```bash
cd projects/15-phishing-awareness
python3 -m http.server 8080
```

Open http://127.0.0.1:8080/ . This server only shares this folder on your own computer.

## Portfolio deliverable

A screenshot of the two messages and your score, plus one real example you rewrote into the safer style (no real company secrets).

## Exercise

Score 2/2 on the quiz. Rewrite message A as a safer notice that names the official app and never includes a login link.

