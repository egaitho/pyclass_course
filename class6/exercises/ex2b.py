import yaml
import pyeapi
import ipdb
from getpass import getpass
from my_functions import yml_load_devices,output_printer


#ipdb.set_trace()
def main():
    password = getpass()
    device_dict = yml_load_devices("ex2a.yml")
    print(device_dict)
    print(type(device_dict))
    print()
    print()
    device_dict['password'] = password
    connection = pyeapi.client.connect(**device_dict)

    device = pyeapi.client.Node(connection)

    output = device.enable("show ip arp")

    arp_list = output[0]['result']['ipV4Neighbors']
    
    output_printer(arp_list)

if __name__ == "__main__":
    main() 
    
