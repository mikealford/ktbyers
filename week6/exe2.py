from getpass import getpass
from netmiko import Netmiko

password = getpass()

device = {
   'host': '192.168.122.72',
   'username': 'malford',
   'password': password,
   'device_type': 'cisco_ios'
}

net_connect = Netmiko(**device)

output = net_connect.send_command('show ip int br')

print(output)

