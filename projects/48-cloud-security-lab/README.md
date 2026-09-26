# 48 — Cloud security lab

## What this is

`iam_lint.py` reads `sample_policy.json`. The sample allows Action `*`, Resource `*`, and `iam:PassRole` on `*`. The linter prints findings and exits 1. Own accounts only.

## Why it matters

A star in an IAM policy is often a real outage or a real breach later. Least privilege is naming the action and the resource.

## How to run

```bash
python3 projects/48-cloud-security-lab/iam_lint.py projects/48-cloud-security-lab/sample_policy.json
```

The command is supposed to exit 1. That is the finding.

## Portfolio deliverable

The three findings, plus a rewritten statement that allows `s3:GetObject` on one bucket.

## Exercise

Write `tight_policy.json` with no stars and confirm the linter prints `IAM findings` and `none`, then exits 0.
