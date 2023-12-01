import sys

def main():
	if len(sys.argv) != 2:
		print("Please provide an input file")
		return

	sum = 0;
	with open(sys.argv[1], 'r') as file:
		for line in file:
			sum += getvalues(line)

	print("The sum of calibration values is " + str(sum))

	return

def getvalues(line):
	first = -1
	last = -1

	for char in line:
		if char.isdigit():
			if first == -1:
				first = int(char)
			last = int(char)
	
	return first * 10 + last

main()
