#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
password = getpass()

device1 = {'host':'nxos2.lasthop.io',
           'username':'pyclass',
           'password':password,
           'device_type':'cisco_ios',
           'global_delay_factor': 2,
           'session_log':'my_session.txt'}
timenow = datetime.now()
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
output = net_connect.send_command('show lldp neighbor detail', strip_prompt =False, strip_command=False)

print(output)
net_connect.disconnect()
current_time = datetime.now() - timenow
print(f'The time it took to execute is :{current_time}')
