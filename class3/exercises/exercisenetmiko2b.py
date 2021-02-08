#!/usr/bin/env python
from pprint import pprint
import yaml
from netmiko import ConnectHandler

with open("exercise2b.yaml", "r") as f:
    data = yaml.full_load(f)

pprint(data)
