# Linux hardening checklist

Do this on a lab VM. Confirm each line. Do not disable your only way back in.

- [ ] Daily work uses a normal user, not root.
- [ ] `sudo` is limited to the people who need it.
- [ ] UFW default deny incoming is on. SSH is allowed only from the LAN.
- [ ] SSH: `PermitRootLogin no`. Keys instead of passwords if you can still log in.
- [ ] Unneeded services are off.
- [ ] Updates are installed, then the VM is snapshotted.
- [ ] Shared folders to the host are off unless you need them for this exercise.
