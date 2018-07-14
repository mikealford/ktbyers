import random

def random_num(network='10.10.10.'):
	last_octet = random.randint(1, 254)
	result = network + str(last_octet)
	return result

print('\n')
print(random_num())
print(random_num('192.168.1.'))
print(random_num(network='172.16.31.'))
print('\n')
