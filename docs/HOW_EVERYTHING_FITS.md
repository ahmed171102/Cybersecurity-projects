# How everything fits

Security is a stack. The bottom has to exist or the top is a document nobody can enforce.

```text
policies          who may do what, how data is labeled, how you recover
apps and identity logins, roles, tokens, object checks
data protection   encryption, hashes, backups, privacy delete
detection         logs, alerts, timelines, dashboards
hosts and networks  addresses, firewalls, VLANs, hardening
```

## Hosts and networks

Projects 01–06, 17–22. If you cannot name the subnet, the port, and the firewall rule, a fancy dashboard has nothing honest to show.

## Detection

Projects 14, 27, 28, 29, 34, 36, 52. Logs become events. Events become alerts. Alerts become a timeline and a status: open, triaging, or closed.

## Data protection

Projects 07–11, 24–26. Encrypt what you store, hash what you must fingerprint, and keep a backup you can check. Project 25 is the privacy piece: export one person’s data, then delete it.

## Apps and identity

Projects 12, 23, 31, 35, 49. Unique users, least privilege, hashed passwords, tokens that expire, and a check that the caller owns the record. Project 35 stops a secret from being committed beside that app.

## Policies

Projects 32, 37, 38, 50. The threat model says what you worried about. The policy says who may see confidential data and how fast you must recover. The capstone is the short list a small company can actually finish. The report is how a test becomes work for someone else.
