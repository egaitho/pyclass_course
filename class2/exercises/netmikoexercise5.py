
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {"host":"nxos1.lasthop.io",
           "username":"pyclass",
           "password":password,
           "device_type":"cisco_nxos",
           "session_log":"mylog.log"
           }

device2 = {"host":"nxos2.lasthop.io",
           "username":"pyclass",
           "password":password,
           "device_type":"cisco_nxos",
           "session_log":"mylog1.log"
           }

mydevices = [device1,device2]

for device in mydevices:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_config_from_file("deviceconfig.txt", strip_prompt = False, strip_command = False)
    print(output)
    net_connect.save_config()
    

net_connect.disconnect()
