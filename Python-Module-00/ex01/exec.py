import sys


strings = ""



if (len(sys.argv) == 1):
	print("usage: python3 exec.py <ONE OR MORE STRINGS>")
	exit()


if (len(sys.argv) > 1):
	for s in sys.argv[1:]:
		if (strings == ''):
			strings = s
		else:
			strings = strings + ' ' + s

print(strings[::-1].swapcase())
