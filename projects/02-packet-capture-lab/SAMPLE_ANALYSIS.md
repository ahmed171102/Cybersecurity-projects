# Sample DNS and TCP analysis

The synthetic story in `generate_synthetic_pcap_notes.py` is the whole case.

- Packets 1–2 prove the laptop can reach its gateway. That is local connectivity, not the internet.
- Packets 3–4 are DNS. The question is the name `example.com`. The answer in this story is the documentation address `203.0.113.50`, which is not a host you should contact.
- Packets 5–7 are the TCP three-way handshake to port 443. SYN opens, SYN-ACK agrees, ACK confirms. Only then would TLS start. This file does not include an attack.

Only capture networks you own.
