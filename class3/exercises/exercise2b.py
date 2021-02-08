#!/usr/bin/env python
from pprint import pprint
import yaml


arista4 = {"device_name":"arista4", "hostname":"arista4.lasthop.io"}
srx2 = {"device_name":"srx2", "hostname":"srx2.lasthop.io"}
nxos1 = {"device_name":"nxos1", "hostname":"nxos1.lasthop.io"}
nxos2 = {"device_name":"nxos2","hostname":"nxos2.lasthop.io"}

my_devices = [arista4,srx2,nxos1,nxos2]

for device in my_devices:
    device["username"] = "admin"
    device["password"] = "cisco123"
with open("exercise2b.yaml", "wt") as f:
    yaml.dump(my_devices, f)    
