

def convert_mac(mac_addr):
	mac_addr = mac_addr.split('.')
	mac_addr = ''.join(mac_addr)
	mac_addr = mac_addr.upper()
	new_mac = []
	while len(mac_addr) > 0:
		two_digits = mac_addr[:2]
		mac_addr = mac_addr[2:]
		new_mac.append(two_digits)
	new_mac = ":".join(new_mac)
	return new_mac


print(convert_mac('1111.ffff.gggg'))
print(convert_mac('1111.ffff.20ee'))
print(convert_mac('a:b:c:d:e:f'))
