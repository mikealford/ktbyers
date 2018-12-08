from getpass import getpass 
from netmiko import Netmiko

password = getpass()

device = {
   'host': '192.168.122.72',
   'username': 'malford',
   'password': password,
   'device_type': 'cisco_ios'
}

ios_commands = ['logging trap alerts', 'spanning-tree portfast bpduguard default']
net_connect = Netmiko(**device)

net_connect.send_command_set(ios_commands)
net_connect.send_config_from_file('cmd_file')

