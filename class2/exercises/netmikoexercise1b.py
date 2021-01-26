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

output = net_connect.send_command("ping", expect_string=r'ip', strip_prompt= False, strip_command = False)

output += net_connect.send_command("\n", expect_string=r'address', strip_prompt=False, strip_command=False)
output += net_connect.send_command("8.8.8.8", expect_string=r'Repeat count', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'size', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'seconds', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'commands', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'sizes', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'#', strip_prompt=False, strip_command=False)

print(output)
net_connect.disconnect()
