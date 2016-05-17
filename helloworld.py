import sys

def main(argv):
	if (len(argv)>0):
		print("Hello "+argv[0]+"!")
	else:
		print("Hello world!")

if __name__ == "__main__":
    main(sys.argv[1:])
