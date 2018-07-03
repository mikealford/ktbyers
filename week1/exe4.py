show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version_strip = show_version.strip()
show_version_split = show_version.split()

model = show_version_split[1]
serial_number = show_version_split[2]

print(80 * '-')
print("Is Cisco the vendor? {}".format('cisco' in model.lower()))
print("Is 881 the model? {}".format('881' in model.lower()))
print("\n")
print("The model is: {}".format(model))
print("The serial number is: {}".format(serial_number))
print(80 * '-')



