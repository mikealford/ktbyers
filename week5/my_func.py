
def print_ip(ip_addr, username='admin', password='cisco123'):
	print("My IP address is: {}".format(ip_addr))
	print(username)
	print(password)
	return

print_ip("10.1.1.1")
print_ip("10.1.1.2")
print_ip("10.1.1.3")
