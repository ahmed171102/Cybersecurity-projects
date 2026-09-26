# 13 — Web app security checklist

## What this is

`check_headers.py` requests one HTTPS URL and looks for CSP, HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, and Permissions-Policy. `AUDIT_TEMPLATE.md` is the write-up.

## Why it matters

These headers tell the browser to apply extra limits. They are a normal first check on an application you are allowed to review.

## How to run

```bash
python3 projects/13-webapp-security-checklist/check_headers.py https://example.com
```

`example.com` is a fair public documentation site. Your school's portal is not, unless they asked for the check.

## Portfolio deliverable

A filled audit template for a site you own, or for `example.com`, with one sentence per missing header.

## Exercise

Check https://example.com and fill AUDIT_TEMPLATE.md. Add a note for each missing header that says what the browser would do if it were present.

