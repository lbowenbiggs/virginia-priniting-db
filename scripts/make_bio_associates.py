import csv

# Takes a CSV File in the form of (biography_id, name, associate_list)
# The CSV File should be named bio_associates_unparsed.csv and be in the same directory as the script.
# The associate list is a list of names with biography_ids in parenthesis
# eg: "Adams (001), Smith (002)"

# Redirect the output to a CSV:
# $ python make_bio_associates.py > bio_associates.csv
# (You may need to explicitly run with python3)

global_id_count = 1

def make_associate(person, associate_list):
	for associate in associate_list:
		try:
			global global_id_count
			print(global_id_count, ",", person, ",", int(associate[:3]))
			global_id_count = global_id_count + 1
			# Association is a symmetrical relationship, so add the reverse to the table too
			print(global_id_count, ",", int(associate[:3]), ",", person)
			global_id_count = global_id_count + 1
		except ValueError:
			pass

with open('bio_associates_unparsed.csv', newline='') as csvfile:
	crdr= csv.reader(csvfile, delimiter=',')
	for row in crdr:
		make_associate(row[0], row[2].split("("))
