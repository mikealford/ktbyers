from __future__ import unicode_literals, print_function

with open("show_arp.txt") as f:
	show_arp = f.read()

show_arp = show_arp.splitlines()

#Remove first line
show_arp = show_arp[1:]

gateway_found = False
arista_found = False

#Iterate over each line storing the IP and Mac into separate variables.
#Check if IP matches certain values.
#Use True/False to exit loop when both entries are found.

for line in show_arp:
	fields = line.split()
	ip_addr = fields[1]
	mac_addr = fields[3]
	if gateway_found and arista_found == True:
		print("Exiting")
		break
	elif ip_addr == '10.220.88.1':
		print("Default gateway IP/Mac is: {} {}".format(ip_addr, mac_addr))
		gateway_found = True
	elif ip_addr == '10.220.88.30':
		print("Arista3 IP/Mac IP is: {} {}".format(ip_addr, mac_addr))
		arista_found = True




