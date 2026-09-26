# 12 — RBAC demo

## What this is

Three users: alice the admin, bob the analyst, carol the guest. An action is allowed only if that role has it.

## Why it matters

Logging in is not the same as being allowed to delete users. Least privilege is this table, written down.

## How to run

```bash
python3 projects/12-rbac-demo/rbac.py --user alice --action delete_users
python3 projects/12-rbac-demo/rbac.py --user carol --action delete_users
```

Alice prints ALLOW. Carol prints DENY and the process exits 1.

## Portfolio deliverable

Both outputs, and one extra action you added for bob only.

## Exercise

Run alice delete_users (ALLOW) and carol delete_users (DENY). Then: python rbac.py --user bob --action delete_users --explain

