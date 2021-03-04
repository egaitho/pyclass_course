import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
            transport = "https",
            host = "arista3.lasthop.io",
            username = "pyclass",
            password = getpass(),
            port = "443")

device = pyeapi.client.Node(connection)

output = device.enable("show ip arp")
for list in output:
    for k,v in list.items():
        if k == 'result':
            for key,value in v.items():
                if key == 'ipV4Neighbors':
                    for n in range(len(value)):
                        print(f"{value[n]['address']} {value[n]['hwAddress']}")


