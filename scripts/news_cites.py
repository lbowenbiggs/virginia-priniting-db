#!/usr/bin/env python
import sys

if (len(sys.argv) > 2):
	fname = sys.argv[1]
	startat = sys.argv[2]
	endat = ""
	if (len(sys.argv) == 4):
		endat = sys.argv[3]


#	print("Reading from:", fname)
#	print("Starting at:", startat)
#	print("Ending at:", endat)
#	print("")
	save_str = ""
	infile = open(fname, newline='')

	lineage_num = ""

	reading = False
	linenum = 0
	for line in infile:
		linenum = linenum + 1
		variant_num = ""

		if (linenum == 2):
			lineage_num = line.lower()

		if (line.startswith("Variant")):
			variant_num = lineage_num.strip() + "-" + line.split()[1][0:2]
			save_str = save_str + variant_num + "\t"
		elif (line.startswith(startat)):
			reading = True
		elif (line.startswith(endat) and endat != ""):
			reading = False
			save_str = save_str + "\n"
		else:
			if (reading):
				save_str = save_str + line
	print(save_str)
else:
	print("Usage:")
	print(sys.argv[0], "<filename> <start delimiter> [stop delimiter]")
	print("If no stop delimiter is given, it will read until the end of file")
