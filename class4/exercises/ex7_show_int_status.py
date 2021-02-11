import textfsm

template = open("ex2_show_int_status.tp")

with open("ex2_show_int_status.txt") as f:
    raw_data = f.read()
#import ipdb
#ipdb.set_trace()
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_data)


template.close()
