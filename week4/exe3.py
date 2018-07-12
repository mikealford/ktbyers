import re

with open("show_version.txt") as f:
	show_ver = f.read()

os_version = re.search(r"\d.", show_ver).group(0)

serial_num = re.search(r"", show_ver)
config_register = re.search(r"", show_ver)


print("\n")
print("OS Version: {}".format(os_version))
print("Serial Number: {}".format(serial_num))
print("Config Register: {}".format(config_register))
print("\n")
