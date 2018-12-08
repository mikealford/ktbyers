from getpass import getpass 
from netmiko import Netmiko

password = getpass()

device = {
   'host': '192.168.122.74',
   'username': 'malford',
   'password': password,
   'device_type': 'arista_eos'
}

net_connect = Netmiko(**device)
filename = 'small_file.txt'
cmd = 'delete flash:{}'.format(filename)

output = net_connect.send_command_timing(cmd)

if 'confirm' in output:
	output += connect_connect.send_command_timing('\n')

print(output)

