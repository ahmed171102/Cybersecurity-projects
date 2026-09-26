# 04 — DNS resolver

## What this is

A small lookup tool. It asks for A, AAAA, MX, CNAME, TXT, and NS records.

## Why it matters

Almost every connection starts with a name. If you can read the record types, you can tell a website address from a mail server.

## How to run

```bash
python3 projects/04-dns-resolver/resolve.py example.com
```

`example.com` is a documentation name and a fair query. Do not use this as a scanner against a list of companies.

## Portfolio deliverable

The output for one domain, with a sentence on which record a browser uses and which record mail uses.

## Exercise

Look up example.com and write which record a browser uses (A or AAAA) and which record mail uses (MX).

