from my_devices import network_devices
from my_functions import open_napalm_connection
from my_functions import create_checkpoint

if __name__ == "__main__":
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)
   # for conn in connections:
    #    create_checkpoint(conn)

    for conn in connections:
        conn.load_replace_candidate(filename="nxos1.checkpoint")
        print(conn.compare_config())
        conn.discard_config()
        print(conn.compare_config())
    
        conn.close()

