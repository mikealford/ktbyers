from pprint import pprint

with open("show_vlan.txt") as f:
	show_vlan = f.read()

vlan_list = []

for line in show_vlan.splitlines():
	if 'active' in line:
		fields = line.split()
		vlan_id = fields[0]
		vlan_name = fields[1]
		vlan_list.append((vlan_id, vlan_name))

print()
pprint(vlan_list)
print()	
