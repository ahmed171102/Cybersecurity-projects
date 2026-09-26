# Wireshark and tcpdump cheatsheet

Only capture networks you own. A lab VM on a host-only adapter is the right place.

## tcpdump

```bash
sudo tcpdump -i any -c 10 -n
sudo tcpdump -i any -c 20 -n port 53
sudo tcpdump -i any -c 20 -n tcp port 443
```

`-i any` is every interface on that VM. `-c 10` stops after 10 packets. `-n` skips name lookups.

## Wireshark display filters

| Filter | Shows |
| --- | --- |
| `icmp` | ping |
| `dns` | name lookups |
| `dns.qry.name == "example.com"` | one name |
| `tcp.port == 443` | web sessions |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | start of a handshake |

A handshake is SYN, then SYN-ACK, then ACK. After that, the bytes belong to the application.
