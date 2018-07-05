from __future__ import unicode_literals, print_function

with open("show_lldp_neighbors_detail.txt") as f:
	show_lldp = f.read()

fields = []

retrieved_system_name = False
retrieved_port_id = False

print(show_lldp[0])
print("Port id" in show_lldp[2])

for line in show_lldp:
	if retrieved_system_name and retrieved_port_id == True:
		print("System Name: {}".format(system_name))
		print("Port id: {}".format(port_id))
	elif "Port id:" in line:
		fields = line.split()
		print(fields)
		port_id = fields[1]
		retrieved_port_id = True
	elif "System Name:" in line:
                fields = line.split()
                system_name = fields[1]
                retrieved_system_name = True

