from my_devices import network_devices
from my_functions import open_napalm_connection

if __name__ == "__main__":
    connections = []

    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

    for conn in connections:
        filename = f"{conn.hostname}-loopbacks"
        conn.load_merge_candidate(filename=filename)
        print("Compare configurations after merging")
        print()
        print(conn.compare_config())
        conn.commit_config()
        print("compare configs after commit")
