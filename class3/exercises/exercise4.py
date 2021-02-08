#!/usr/bin/env python

from pprint import pprint
import json

with open("exercise4.json") as f:
    arp_data = json.load(f)
arp_dict = {}
arp_data = arp_data['ipV4Neighbors']
for arp_entry in arp_data:
    ip_addr = arp_entry['address']
    mac_addr = arp_entry['hwAddress']
    arp_dict.update({ip_addr:mac_addr})

pprint(arp_dict)
