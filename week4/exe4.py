import re

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''


match = re.search(r"^Cisco (?P<model>\S+).* with (?P<memory>\S+) bytes of memory", show_version, flags=re.M)
model = match.groupdict()['model']
memory = match.groupdict()['memory']

print()
print('-' * 80)
print("Model: {}".format(model))
print("Memory: {}".format(memory))
print('-' * 80)
print()
