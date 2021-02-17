from __future__ import unicode_literals, print_function
import time
import re

from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment
from my_devices import nxos1, nxos2
from netmiko import ConnectHandler
from getpass import getpass

if __name__ == "__main__":
    
    env=Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader("./Template/exercise2/")
    template_file = "jinja2ex2c.j2"
    
    password = getpass("Please enter the device password: ")
    interface = "Ethernet1/3"
        
    nxos1_vars = {"interface":interface,"ip_address":"10.23.23.1","ipv4_mask":24,"local_as":22}
    nxos2_vars = {"interface":interface,"ip_address":"10.23.23.2","ipv4_mask":24,"local_as":22} 
    
    nxos1_vars['peerip'] = nxos2_vars['ip_address']
    nxos2_vars['peerip'] = nxos1_vars['ip_address']
    nxos1_vars['device_name'] = "nxos1"
    nxos2_vars['device_name'] = 'nxos2'
   # import ipdb
   # ipdb.set_trace()
        
    nxos1['j2_vars'] = nxos1_vars
    nxos2['j2_vars'] = nxos2_vars

    nxos1['password'] = password
    nxos2['password'] = password
    
    for device in (nxos1,nxos2):
        tmp_device = device.copy()
        j2_var = tmp_device.pop('j2_vars')
        template = env.get_template(template_file)
        cfg = template.render(**j2_var)
        device_name = device['j2_vars']['device_name']
        cfg_lines = [cfg.strip() for cfg in cfg.splitlines()]
        #  login in to the device
        net_connect = ConnectHandler(**tmp_device)
        #saving device login info
        device['ssh_conn'] = net_connect
        print(f">> configurating bgp and interface on {device_name}")
        output = net_connect.send_config_set(cfg_lines)
        print()
        print(output)
        print("\n\n")
                
    sleep_time = 15
    print(f"Sleep for {sleep_time}s to allow bgp to converge")
    time.sleep(sleep_time)

    for device in (nxos1,):
        net_connect = device['ssh_conn']
        remote_ip = device["j2_vars"]['peerip']
        ping_cmd = f"ping {remote_ip}"
        output = net_connect.send_command(ping_cmd)
        if "64 bytes from" not in output:
            print()
            print(f"The remote ip {remote_ip} is unreachable")
        else:
            print()
            print(f"The remote ip {remote_ip} is reachable")
        bgp_status = f"show ip bgp summary | include {remote_ip}"
        output = net_connect.send_command(bgp_status)
        match = re.search(r"\s+(\S+)\s*$",output)
        prefix_received = match.group(1)        
        try:    
            prefix_received =int(prefix_received)
            print()            
            print(f"The bgp is established with {prefix_received} prefix received")
        except ValueError:
            print()
            print("The bgp is not established")

for device in (nxos1,nxos2):
    net_connect = device['ssh_conn']
    net_connect.disconnect()
     
