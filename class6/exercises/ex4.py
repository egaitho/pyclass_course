from my_function_arista import load_yaml_devices
import pyeapi
from jinja2 import StrictUndefined,FileSystemLoader
from jinja2.environment import Environment
from getpass import getpass

def main():
    devices = load_yaml_devices()

    my_devices = devices.pop("my_devices")
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")
    template_file = "ex4.j2"
    password = getpass() 
    
    eapi_devices = []
    for device,devices_info in devices.items():
        temp_devices_info = devices_info.copy()
        j2_var = temp_devices_info.pop("j2_var")
        template = env.get_template(template_file)
        output_data = template.render(**j2_var)
        cfg = output_data.strip().splitlines()
        temp_devices_info['password'] = password
        connection = pyeapi.client.connect(**temp_devices_info)
        arista_device = pyeapi.client.Node(connection)
        eapi_devices.append(arista_device)
        output = arista_device.config(cfg)
        print()
        print(device)
        print(output)
        print()
        #confirm ip route after config
    for device in eapi_devices:
        
        output = device.enable("show ip interface brief")
        print()
        print("-"*50)
        print(output[0]['result']['output'].rstrip())       
        print("-"*50)
        
              


if __name__ == "__main__":
    main()
