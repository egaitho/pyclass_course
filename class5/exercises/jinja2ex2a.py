from __future__ import unicode_literals, print_function
from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment


env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./Template/exercise2/")

interface = "Ethernet1/1"
nxos1 = {"interface":interface,"ip_address":"10.1.100.1","ipv4_mask":24}
nxos2 = {"interface":interface,"ip_address":"10.1.100.2","ipv4_mask":24}

import ipdb
ipdb.source()
for my_var in (nxos1,nxos2):
    my_temp = env.get_template("jinja2ex2a.j2")
    output = my_temp.render(**my_var)
    print()
    print(output)
    print()
