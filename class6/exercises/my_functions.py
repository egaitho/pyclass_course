import yaml

def yml_load_devices(filename="ex2a.yml"):
    with open(filename, "r") as f:
        return yaml.load(f,Loader=yaml.FullLoader)
    raise ValueError("Reading yaml file failed")

def output_printer(arp_list):
    print()
    print("-"*30)
    for arp_entry in arp_list:
        mac_address = arp_entry['hwAddress']
        ip_address = arp_entry['address']
        print(f"{mac_address} ----> {ip_address}")
    print("-"*30)
    print()

yml_load_devices()
