# 08 — Password checker

## What this is

A local score from 0 to 5 and a rough entropy estimate. A short common-password list forces those values to 0. The password is not written to disk and not sent anywhere.

## Why it matters

Length and variety matter more than a clever word. A password that is already on a common list is a bad password even if it looks complicated to you.

## How to run

```bash
python3 projects/08-password-checker/check_password.py --password "Summer2024!"
```

The process list can show command-line arguments. For a real password, type it into a prompt you add yourself, or use a throwaway example as above.

## Portfolio deliverable

Two scores side by side: `password` and a longer passphrase, with one sentence on entropy.

## Exercise

Score password and a 16-character passphrase. Then add one word to common.txt and confirm that word now scores 0.

