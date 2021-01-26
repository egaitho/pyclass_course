#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
password = getpass()

device1 = {'host':'cisco4.lasthop.io',
           'username':'pyclass',
           'password':password,
           'device_type':'cisco_ios',
#           'global_delay_factor': 2,
           'session_log':'my_session.txt'}
#timenow = datetime.now()
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
output = net_connect.send_command('show lldp neighbors', use_textfsm= True, strip_prompt =False, strip_command=False)

print(output)

output1 = net_connect.send_command('show version', use_textfsm = True, strip_prompt = False, strip_command = False)

print("\n\n--------------------")

print(output1)
print("\n\n--------------------")
print(f"The neighbor interface connected to the cisco device is :{output[0]['neighbor_interface']}")
net_connect.disconnect()
#current_time = datetime.now() - timenow
#print(f'The time it took to execute is :{current_time}')
