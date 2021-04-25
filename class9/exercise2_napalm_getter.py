from my_devices import network_devices
from my_functions import open_napalm_connection
from pprint import pprint
from my_functions import create_backup

if __name__ == "__main__":
    connections = []

    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

    for conn in connections:
        pprint(conn.get_arp_table())
        print()
        try:
            print(conn.get_ntp_peers())
        except:
            print("get ntp peers is not available")
        
    for conn in connections:
        create_backup(conn)
        conn.close()





