# 25 — Privacy

## What this is

Seeds two fake people, lists the inventory, exports `user_1` to JSON, and deletes `user_1`. Nothing here is a real customer.

## Why it matters

Privacy work is export and delete, not a banner. If you cannot remove one person, you do not control the data.

## How to run

```bash
python3 projects/25-privacy-gdpr/privacy.py seed
python3 projects/25-privacy-gdpr/privacy.py inventory
python3 projects/25-privacy-gdpr/privacy.py export user_1
python3 projects/25-privacy-gdpr/privacy.py delete user_1
```

## Portfolio deliverable

The export file and the inventory after the delete, showing `user_2` still present and `user_1` gone.

## Exercise

Seed, export user_1, delete user_1, inventory. user_2 must remain. Open the export JSON and confirm it is only user_1.

