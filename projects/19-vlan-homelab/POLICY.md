# VLAN policy

| VLAN | Name | Range | Who starts connections |
| --- | --- | --- | --- |
| 10 | trusted | 192.168.10.0/24 | Laptops and phones. May reach the internet. |
| 20 | IoT | 192.168.20.0/24 | Bulbs and cameras. May reach the internet only if you need updates. Must not start connections to VLAN 10. |
| 30 | lab | 192.168.30.0/24 | Practice VMs. No route to VLAN 10. |

Default deny between VLANs. Add an allow only when you can name the device and the port. The IoT network does not get to open sessions toward the trusted network.
