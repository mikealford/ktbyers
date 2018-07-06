from __future__ import unicode_literals, print_function
import os

ip_list = []
base_ip = '10.10.100.'

#Create a list of IP Addresses
for last_octet in range(1,255):
	new_ip = base_ip + str(last_octet)
	ip_list.append(new_ip)

#Enumerate the list of IP Addreses
for ip in enumerate(ip_list):
	print(ip)

#Create a subset list of IP Addresses
new_list = ip_list[2:6]
print()
print()
print(new_list)
print()
print()

#Ping each of the new list
for each in new_list:
	print("IP Addr: ", each)
	return_code = os.system("ping -c 2 {}".format(each))



