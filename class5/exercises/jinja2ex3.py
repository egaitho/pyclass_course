from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader("./Template/exercise3/")
#import ipdb
#ipdb.set_trace()
my_var = {"vrf_name":"blue","route_distinguisher":"100.1","ipv4_enabled":True,"ipv6_enabled":True}

template_file = "jinja2ex3.j2"
template = env.get_template(template_file)
output = template.render(**my_var)
print()
print(output)
print()
