#!/usr/bin/env python
from netmiko import ConnectHandler
import yaml

with open('/home/egaitho/.netmiko.yml') as f:
    netmiko_data = yaml.load(f)

session = ConnectHandler(**netmiko_data['cisco3'])
print(session.find_prompt())

