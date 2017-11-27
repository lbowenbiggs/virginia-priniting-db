import sys

if (len(sys.argv) > 2):
	fname = sys.argv[1]
	startat = sys.argv[2]
	endat = ""
	if (len(sys.argv) == 4):
		endat = sys.argv[3]


	print("Reading from:", fname)
	print("Starting at:", startat)
	print("Ending at:", endat)
	print("")

	infile = open(fname, newline='')
	save_str = ""
	reading = False
	for line in infile:
		if (line.startswith(startat)):
			reading = True
		elif (line.startswith(endat) and endat != ""):
			reading = False
			break
		else:
			if (reading):
				save_str = save_str + line
	print(save_str)
else:
	print("Usage:")
	print(sys.argv[0], "<filename> <start delimiter> [stop delimiter]")
	print("If no stop delimiter is given, it will read until the end of file")
