import yaml
import pyeapi
import ipdb
from getpass import getpass
from my_functions import yml_load_devices,output_printer



#ipdb.set_trace()
def main():
    password = getpass()
    device_dict = yml_load_devices("ex2a.yml")
    device_dict['password'] = password
    connection = pyeapi.client.connect(**device_dict)

    device = pyeapi.client.Node(connection)

    output = device.enable("show ip route")
    
    output1 = output[0]['result']['vrfs']['default']['routes']
    
    for ip_prefix, route_values in output1.items():
        prefix = ip_prefix
        route_type = route_values['routeType']
        if route_type == 'static':
            next_hop = route_values['vias'][0]['nexthopAddr']
            print(f"PREFIX: {prefix} ROUTE_TYPE: {route_type} NEXT_HOP {next_hop}")
        else:
            interface = route_values['vias'][0]['interface']
            print(f"PREFIX: {prefix} ROUTE_TYPE: {route_type} INTERFACE: {interface}")

if __name__ == "__main__":
    main() 
    
