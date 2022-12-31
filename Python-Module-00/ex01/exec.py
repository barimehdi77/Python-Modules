import sys


strings = ""



if (len(sys.argv) == 1):
	print("usage: python3 exec.py <ONE OR MORE STRINGS>")
	exit()


if (len(sys.argv) > 1):
	for str in sys.argv[1:]:
		if (strings == ''):
			strings = str
		else:
			strings = strings + ' ' + str

print(strings[::-1].swapcase())
# for thing in sys.argv:
# 	print(thing, end=" ")
