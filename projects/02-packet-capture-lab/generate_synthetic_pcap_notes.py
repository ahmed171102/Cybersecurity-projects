"""Print a 7-packet story. This does not capture traffic."""

from __future__ import annotations


PACKETS = [
    "1  ICMP echo request   laptop -> 192.168.1.1     ping, one shot",
    "2  ICMP echo reply     192.168.1.1 -> laptop     the gateway answered",
    "3  DNS query           laptop -> 192.168.1.1     name example.com, type A",
    "4  DNS response        192.168.1.1 -> laptop     example.com -> 203.0.113.50 (documentation address)",
    "5  TCP SYN             laptop -> 203.0.113.50:443   start of the handshake",
    "6  TCP SYN-ACK         203.0.113.50:443 -> laptop   the server accepted the start",
    "7  TCP ACK             laptop -> 203.0.113.50:443   handshake done, HTTP can ride inside TLS",
]


def main() -> None:
    print("Synthetic capture notes. Only capture networks you own.")
    print("Story: ping the gateway, resolve example.com, complete a TCP handshake to port 443.\n")
    for line in PACKETS:
        print(line)
    print("\nCount: 7 packets. Ping is 1-2, DNS is 3-4, TCP handshake is 5-7.")


if __name__ == "__main__":
    main()
