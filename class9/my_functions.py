from napalm import get_network_driver


def open_napalm_connection(device):
    my_device = device.copy()
    device_type = my_device.pop("platform")
    driver = get_network_driver(device_type)
    conn = driver(**my_device)
    conn.open()
    return conn

def create_backup(conn):
    backup = conn.get_config()
    filename = f"{conn.hostname}-running.txt"
    with open(filename, "w") as f:
        f.write(backup['running'])

def create_checkpoint(conn):
    checkpoint = conn._get_checkpoint_file()
    with open(f"{conn.hostname}-checkpoint", "w") as f:
        f.write(checkpoint)
    
