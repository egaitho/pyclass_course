from getpass import getpass

password = getpass()

cisco3 = dict(
    hostname = "cisco3.lasthop.io",
    username = "pyclass",
    password = password,
    platform = "ios",
    )

arista1 = dict(
    hostname = "arista1.lasthop.io",
    username = "pyclass",
    password = password,
    platform = "eos",
    )
nxos1 = dict(
    hostname = "nxos1.lasthop.io",
    username = "pyclass",
    password = password,
    platform = "nxos",
    optional_args = {"port":8443}
    )
    
network_devices = [nxos1]    
