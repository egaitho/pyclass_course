from napalm import get_network_driver
from my_devices import network_devices
from pprint import pprint


def napalm_connection(device):
    my_device = device.copy()
    device_type = my_device.pop("platform")
    driver = get_network_driver(device_type)
    conn = driver(**my_device)
    conn.open()
    return conn

if __name__ == "__main__":
    connections = []

    for device in network_devices:
        conn = napalm_connection(device)
        connections.append(conn)
    
    for conn in connections:
        print()
        print(conn)
        print()
        print(f"{conn.platform} facts")
        print()
        pprint(conn.get_facts())

    
    
