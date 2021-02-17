#!/usr/bin/env python
from jinja2 import StrictUndefined,FileSystemLoader
from jinja2.environment import Environment
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

#password = getpass("Please input the router password: ")
#device1 = {"host":"cisco3.lasthop.io","device_type":"cisco_ios","username":"pyclass", "password":password}

#net_connect = ConnectHandler(**device1)
#print(net_connect.find_prompt())

#output = net_connect.send_command("show run")
#pprint(output)
#with open("cisco3_config.j2", "wt") as f:
 #   f.write(output)
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

my_var = {"ntp1":"130.126.24.24","timezone_dst":"PDT","ntp2":"152.2.21.1","timezone":"PST","timezone_offset":"-8"}

template = "cisco3_config.j2"

my_template = env.get_template(template)
output1 = my_template .render(**my_var)
print()
print(output1)
print()

