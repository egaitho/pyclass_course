import yaml
import pyeapi
from getpass import getpass

with open("ex2a.yml") as f:
    device_dict = yaml.load(f)

password = getpass()

device_dict['password'] = password

connection = pyeapi.client.connect(**device_dict)

device = pyeapi.client.Node(connection)

output = device.enable("show ip arp")

arp_info = output[0]['result']['ipV4Neighbors']

for arp_entry in arp_info:
    mac_address = arp_entry['hwAddress']
    ip_address = arp_entry['address']
    print(f"{ip_address} {mac_address}")
