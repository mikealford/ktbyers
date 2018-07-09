

net_device = {
'ip_addr':'10.5.6.6',
'vendor':'cisco',
'platform':'ios',
'username':'malford',
'password':'chicken',
}

bgp_fields = {
'bgp_as':'65002',
'peer_as':'20551',
'peer_ip':'10.232.232.2'
}

net_device.update(bgp_fields)


print("These are the dictionary keys: ")
for x in net_device:
	print(x)

print('\n')
print('\n')

print("These are the keys and values: ")
for x in net_device.items():
	print(x)



