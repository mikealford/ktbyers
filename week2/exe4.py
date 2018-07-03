with open("show_ip_int_brief.txt") as f:
	output = f.readlines()

fa4 = output[5]
fa4 = fa4.split()

interface = fa4[0]
ip_addr = fa4[1]

result = (interface, ip_addr)
print(result)
