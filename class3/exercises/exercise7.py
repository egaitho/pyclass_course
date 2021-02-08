#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse


bgp_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out"""

my_conf = CiscoConfParse(bgp_config.splitlines())

bgp_peer = []

bgp_neighbor = my_conf.find_objects_w_parents(parentspec=r"router bgp", childspec=r"neighbor")
for neighbor in bgp_neighbor:
    _,neighbor_ip = neighbor.text.split()
    for child in neighbor.children:
        if "remote-as" in child.text:
            _,remote_as=child.text.split()
    bgp_peer.append((neighbor_ip,remote_as))
print()
print("BGP Peers:")
print(bgp_peer)
print()
