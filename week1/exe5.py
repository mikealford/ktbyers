mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1_split = mac1.split()
mac2_split = mac2.split()
mac3_split = mac3.split()

mac_addr1 = mac1_split[3]
mac_addr2 = mac2_split[3]
mac_addr3 = mac3_split[3]

ip_addr1 = mac1_split[1]
ip_addr2 = mac2_split[1]
ip_addr3 = mac3_split[1]

print("")
print("{:>20}{:>20}".format("IP ADDRESS","MAC ADDRESS"))
print('-' * 40)
print("{:>20}{:>20}".format(ip_addr1,mac_addr2))
print("{:>20}{:>20}".format(ip_addr2,mac_addr2))
print("{:>20}{:>20}".format(ip_addr3,mac_addr3))
print("")
