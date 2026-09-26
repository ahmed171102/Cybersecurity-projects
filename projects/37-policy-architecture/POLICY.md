# Policy architecture

## Data classification

| Label | Examples | Who may see it |
| --- | --- | --- |
| public | marketing site | anyone |
| internal | staff wiki | staff accounts |
| confidential | customer notes | named roles |
| restricted | admin secrets | two named people plus the vault |

## Access

- Unique accounts. No shared `admin` login.
- MFA on remote and admin paths.
- Least privilege: the role table is the product (see project 12).
- Offboarding: disable the account the same day the person leaves.

## Backup and recovery

- Daily encrypted backups.
- Recovery point objective (RPO): 24 hours. You can lose at most one day of data.
- Recovery time objective (RTO): 8 hours. The service is back the same working day.
- Restore test: once a quarter, on a lab copy, not only on paper.
