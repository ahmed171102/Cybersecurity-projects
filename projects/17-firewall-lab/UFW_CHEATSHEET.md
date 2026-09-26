# UFW cheat sheet

Run this on a Linux lab VM, not on a laptop you need for class until you have a console backup.

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 192.168.1.0/24 to any port 22 proto tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose
```

That is: deny incoming by default, allow SSH only from the LAN, allow web on 80 and 443. Do not allow 3389. Read `policy_sim.py` for the same idea without changing a live firewall.
