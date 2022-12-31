import sys



if (len(sys.argv) == 1):
	print("usage: python3 whois.py <INT NUMBER>")
	exit()

if (len(sys.argv) > 2):
	print("AssertionError: more than one argument are provided")
	exit()

if (sys.argv[1].isnumeric()):
	if int(sys.argv[1]) == 0:
		print("I'm Zero")
		exit()
	elif (int(sys.argv[1]) % 2) == 0:
		print("I'm Even")
		exit()
	else:
		print("I'm Odd")
		exit()
else:
	print("AssertionError: argument is not an integer")
	exit()
