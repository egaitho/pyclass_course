from jinja2 import StrictUndefined, FileSystemLoader
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader("./Template/exercise4/")
#import ipdb
#ipdb.set_trace()
my_var = [{"vrf_name":"blue","route_distinguisher":"100.1","ipv4_enabled":True,"ipv6_enabled":True},
{"vrf_name":"red","route_distinguisher":"100.1","ipv4_enabled":True,"ipv6_enabled":True},
{"vrf_name":"orange","route_distinguisher":"100.1","ipv4_enabled":True,"ipv6_enabled":True},
{"vrf_name":"green","route_distinguisher":"100.1","ipv4_enabled":True,"ipv6_enabled":True},
{"vrf_name":"yellow","route_distinguisher":"100.1","ipv4_enabled":True,"ipv6_enabled":True}]
j2_vars = {"my_var":my_var}
template_file = "jinja2ex4.j2"
template = env.get_template(template_file)
output = template.render(**j2_vars)
print()
print(output)
print()
