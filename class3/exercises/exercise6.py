#!/usr/bin/env python
from netmiko import ConnectHandler
import yaml
from ciscoconfparse import CiscoConfParse
with open('/home/egaitho/.netmiko.yml') as f:
    netmiko_data = yaml.load(f)

session = ConnectHandler(**netmiko_data['cisco4'])
print(session.find_prompt())

output = session.send_command("show run")

cisco_obj = CiscoConfParse(output.splitlines())
cisco_obj
match = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec="^\s+ip address")

for intf in match:
    print(f"Interface Line: {intf.text}")
    child = intf.re_search_children('^\s+ip address')
    for ip_entry in child:
        print(f"Ip Address Line: {ip_entry.text}")
