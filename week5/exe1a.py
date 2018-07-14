
def ssh_conn(ip_addr, username, password):
	print("IP Address: {}".format(ip_addr))
	print("Username: {}".format(username))
	print("Password: {}".format(password))

ssh_conn('192.168.5.1', 'malford', 'cisco123')

print("\n")

ssh_conn(ip_addr='192.168.5.1', username='malford', password='cisco123')

print("\n")

ssh_conn('192.168.5.1', username='malford', password='cisco123')
