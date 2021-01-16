#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {'host':'nxos1.lasthop.io',
           'username':'pyclass',
           'password':password,
           'device_type':'cisco_nxos',
           'session_log':'my_session.txt'}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
with open('show_version_nxos1.txt', 'w') as f:
    f.write(net_connect.send_command('show version'))
net_connect.disconnect()
