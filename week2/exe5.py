with open("show_ip_bgp_summ.txt") as f:
	f = f.readlines()

#Separate out first and last lines from output
first_line = f[0]
second_line = f[-1]

#Grab BGP AS # from end of first line
first_line = first_line.split()
bgp_as = first_line[-1]

#Grab BGP Peer IP Address from beginning of last line
second_line = second_line.split()
bgp_peer = second_line[0]

print("")
print("BGP AS#: {}".format(bgp_as))
print("BGP Peer: {}".format(bgp_peer))
print("")
