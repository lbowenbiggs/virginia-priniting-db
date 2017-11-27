#!/usr/bin/env python
import sys

if (len(sys.argv) > 1):
	fname = sys.argv[1]

	#print("Reading from:", fname)
	
	save_str = ""
	infile = open(fname)
	
	num_lines = 0
	num_newlines = 0
	reading = False
	for line in infile:
		num_lines = num_lines + 1
		if (num_lines == 1):
			save_str = line.split(':')[0].lower() + '\t'
		if (num_newlines > 0 and not line.isspace()):
			reading = True
		elif (line.isspace()):
			num_newlines += 1

		if (reading):
			save_str = save_str + line
	save_str = save_str + "NEWRECORD\n"
	print(save_str)
