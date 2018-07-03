show_version = open("show_version.txt")
output = show_version.read()
show_version.close()

print(output)
print(type(show_version))

with open("show_version.txt") as f:
	f = f.readlines()

print(f)
print(type(f))
