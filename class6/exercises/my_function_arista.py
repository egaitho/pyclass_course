import yaml

def load_yaml_devices(filename="arista_devices_full.yml"):
    with open(filename) as f:
        return yaml.safe_load(f)
    raise ValueError("Reading yaml file failed")
