ip_addr = ['192.168.5.1', '127.2.11.1', '70.2.111.1', '192.18.6.1', '10.20.1.20']

ip_addr.append('5.5.5.5')
ip_addr.extend(['6.6.6.6', '7.7.7.7'])

ip_addr = ip_addr + ['162.66.21.1','162.66.251.150']

print("")
print("Entire list of IP Addresses: {}".format(ip_addr))
print("First IP Address: {}".format(ip_addr[0]))
print("Last IP Address: {}".format(ip_addr[-1]))

ip_addr.pop(0)
ip_addr.pop(-1)
ip_addr.insert(0, '2.2.2.2')

print("")
print("New First IP Address: {}".format(ip_addr[0]))
