# Concepts

Short definitions you should be able to say without notes.

## IP address

A number for a machine on a network. `192.168.1.10` is a private address people use at home. `127.0.0.1` means "this computer". `8.8.8.8` is a public address. The scanners in this repo accept the first two kinds and refuse the third.

## Port

A door on that address. `443` is encrypted web traffic. `53` is DNS. `22` is SSH. An address can have many ports. A closed port means nothing accepted the connection.

## DNS

The phone book. You ask for `example.com`. A resolver returns an address (an A record), an IPv6 address (AAAA), a mail server (MX), or another name (CNAME). Project 04 prints those types.

## TCP and UDP

TCP sets up a connection, delivers bytes in order, and closes it. The chat in project 03 is TCP. UDP sends datagrams without that handshake. DNS often uses UDP. A log of TCP shows a session. A log of UDP shows queries and answers.

## CIA

- **Confidentiality** — the wrong person cannot read it. Encryption serves this.
- **Integrity** — the bytes were not changed in secret. Hashes and checksums serve this.
- **Availability** — the service is there when it should be. Backups and firewalls serve this too, by limiting damage.

## Encryption and hash

Encryption can be reversed if you have the key. Project 07 does that with AES-GCM. A hash cannot be reversed. Project 10 uses SHA-256 to fingerprint a file. If one byte changes, the hash changes. You do not "decrypt" a hash.

## Authentication and authorization

Authentication answers "who is this?". A password or a token does that. Authorization answers "what may this person do?". Project 12 is authorization. Project 23 does both: the password proves who it is, the role decides which route works.

## Vulnerability, threat, and risk

- A **vulnerability** is a weakness, such as a missing check on project 49’s `/account/<id>` route.
- A **threat** is someone or something that could use the weakness.
- **Risk** is how bad that is in this system: how likely, and how much it matters if it happens. Project 40 ranks findings with a score and an asset value so the important ones go first.
