import csv

# Takes a CSV File in the form of (imprint_id, associate_list)
# The CSV File should be named imprint_associates_unparsed.csv and be in the same directory as the script.
# The associate list is a list of names with biography_ids in parenthesis
# eg: "Adams (001), Smith (002)"

# Redirect the output to a CSV:
# $ python make_imprint_associates.py > imprint_associates.csv
# (You may need to explicitly run with python3)

global_id_count = 1

def make_associate(imprint, associate_list):
	for associate in associate_list:
		try:
			global global_id_count
			print(global_id_count, ",", imprint, ",", int(associate[:3]))
			global_id_count = global_id_count + 1
		except ValueError:
			pass

with open('imprint_associates_unparsed.csv', newline='') as csvfile:
	crdr= csv.reader(csvfile, delimiter=',')
	for row in crdr:
		make_associate(row[0], row[1].split("("))
