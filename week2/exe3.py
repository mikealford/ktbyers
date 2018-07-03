from __future__ import unicode_literals
from pprint import pprint

with open("show_arp.txt") as f:
	f = f.readlines()

#Remove header line, sort lines, and store in new list
remove_header = f[1:]
remove_header.sort()
pprint(remove_header)

#Grab first 3 entries
first_three = remove_header[0:3]

item1 = first_three[0]
item1 = item1.split()
item1 = item1[3]
item2 = first_three[1]
item2 = item2.split()
item2 = item2[3]
item3 = first_three[2]
item3 = item3.split()
item3 = item3[3]

arp_entries = [item1,item2,item3]

arp_entries = '\n'.join(arp_entries)


x = open("arp_entries.txt", mode="w")
x.write(arp_entries)
x.flush()
x.close()
