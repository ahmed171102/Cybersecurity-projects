# Sample detection notes

These are ideas for a lab IDS. They are not a live ruleset and they do not describe an attack to run.

| Match | What you do |
| --- | --- |
| TCP/23 | Alert. Telnet is clear text. Prefer SSH on the lab, and do not leave 23 open. |
| TCP/445 | Alert when the source is outside the file-server VLAN. |
| TCP/443 | Pass. Encrypted web is normal. Look at the name and the volume, not the port alone. |
