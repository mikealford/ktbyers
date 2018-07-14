
device_type = 'cisco_ios'

def ssh_conn2(ip_addr, username, password, device_type):
	print("IP Address: {}".format(ip_addr))
	print("Username: {}".format(username))
	print("Password: {}".format(password))

ssh_conn2('192.168.5.1', 'malford', 'cisco123', 'cisco_ios')

print("\n")

ssh_conn2(ip_addr='192.168.5.1', username='malford', password='cisco123', device_type='cisco_ios')

print("\n")

ssh_conn2('192.168.5.1', 'malford', 'cisco123', device_type)

print("\n")

my_list = {
	'ip_addr': '172.16.31.1',
	'username': 'malford',
	'password': 'cisco123',
	'device_type': 'cisco_ios'
}

ssh_conn2(**my_list)


