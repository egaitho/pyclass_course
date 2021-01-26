#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
password = getpass()

device1 = {'host':'cisco3.lasthop.io',
           'username':'pyclass',
           'password':password,
           'device_type':'cisco_ios',
#           'global_delay_factor': 2,
           'session_log':'my_session.txt'}
#timenow = datetime.now()
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
output = net_connect.send_command('ping google.com', use_textfsm= True, strip_prompt =False, strip_command=False)
print("\n\n----------------------------------------")

print(output)
print("\n\n----------------------------------------")
command = ['ip name-server 1.1.1.1',
            'ip name-server 1.0.0.1',
            'ip domain-lookup']
output_cmd = net_connect.send_config_set(command, strip_prompt = False, strip_command = False)
print(output_cmd)

print("\n\n----------------------------------------")
output1 = net_connect.send_command('ping google.com', use_textfsm = False, strip_prompt = False, strip_command = False)

print(output1)
print("\n\n--------------------")

net_connect.disconnect()
#current_time = datetime.now() - timenow
#print(f'The time it took to execute is :{current_time}')
