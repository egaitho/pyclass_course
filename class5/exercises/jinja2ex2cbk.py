import time
import re

from __future__ import unicode_literals, print_function
from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment
from netmiko import ConnectHandler
from getpass import getpass
from my_devices import nxos1,nxos2

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./Template/exercise2/")

interface = "Ethernet1/3"
nxos1_cfg = {"interface":interface,"ip_address":"10.1.79.1","ipv4_mask":24,"peerip":"10.1.79.2","local_as":22}
nxos2_cfg = {"interface":interface,"ip_address":"10.1.79.2","ipv4_mask":24,"peerip":"10.1.79.1","local_as":22}
password = getpass()

my_device = [my_devices.nxos1, my_devices.nxos2]

#import ipdb
#ipdb.set_trace()

for device in my_device:
    if device == my_devices.nxos1:
        session_nxos1 = ConnectHandler(**device)
        print(session_nxos1.find_prompt())
        my_template = env.get_template("jinja2ex2c.j2"
        output = my_template.render(**nxos1)
        cfg_line = [cfg.strip() for cfg in output.splitlines()]
        session.send_config_set(cfg_line)
    else:
        session_nxos2 = ConnectHandler(**device)
        print(session_nxos2.find_prompt())
        my_template = env.get_template("jinja2ex2c.j2"
        output = my_template.render(**nxos2)
        cfg_line = [cfg.strip() for cfg in output.splitlines()]
        session.send_config_set(cfg_line)


sleep_time = 15
print(f"sleeping for {sleeping_time} seconds")
time.sleep(sleep_time)

