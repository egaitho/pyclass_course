
from netmiko import ConnectHandler
from getpass import getpass
from time import sleep

password = getpass()

device =    {
            "host":"cisco4.lasthop.io",
            "username": "pyclass",
            "password":password,
            "secret":password,
            "device_type":"cisco_ios",
            "session_log":"myoutput.log"
            }

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
net_connect.config_mode()
print(net_connect.find_prompt())
net_connect.exit_config_mode()
print(net_connect.find_prompt())
net_connect.write_channel('disable \n')
sleep(2)
print(net_connect.find_prompt())
print(net_connect.read_channel())
net_connect.enable()
print(net_connect.find_prompt())
