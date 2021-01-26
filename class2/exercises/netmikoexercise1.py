#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {'host':'cisco4.lasthop.io',
           'username':'pyclass',
           'password':password,
           'device_type':'cisco_ios',
           'session_log':'my_session.txt'}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command_timing("ping", strip_prompt = False, strip_command = False)

output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)

print(output)
net_connect.disconnect()
