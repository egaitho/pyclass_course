import json
ipv4_list = []
ipv6_list = []

with open("exercise3.json") as f:
        nxos_data = json.load(f)

for intf, ip_entry_info in nxos_data.items():
    for ipv4_or_ipv6, ip_and_prefix in ip_entry_info.items():
        for ip_addr, prefix_length in ip_and_prefix.items():
            if ipv4_or_ipv6 == "ipv4":
                prefix = prefix_length['prefix_length']
                ipv4_list.append(f"{ip_addr}/{prefix}")
            if ipv4_or_ipv6 == "ipv6":
                prefix = prefix_length['prefix_length']
                ipv6_list.append(f"{ip_addr}/{prefix}")

print(ipv4_list)
print(ipv6_list)
