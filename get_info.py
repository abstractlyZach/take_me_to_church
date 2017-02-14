# get_info.py
# retrieves information from the google spreadsheet

import person
import gspread_connection
import phonenumbers

# 1. go to https://console.developers.google.com/iam-admin/projects
# 2. enable drive API
# 3. go to Credentials > New Credentials > Service account key >
#           use defaults and it will download a json file
# 4. insert the downloaded json file for credentials here
# 5. create a google spreadsheet on your own account and "share" it with 
#        the email included in the json file

SPREADSHEET = gspread_connection.connect()

def get_person_by_phone(phone_number, region='US'):
	'''Given a phone number, returns the corresponding Person object. 
	None if they don't exist'''
	# Converts phonen_number into phonenumbers.PhoneNumber object if they aren't already
	if not isinstance(phone_number, phonenumbers.PhoneNumber):
		phone_number = phonenumbers.parse(phone_number, region)

	worksheet = SPREADSHEET.worksheet("People")

	phone_number_column = get_column_index("phone number", worksheet)
	id_column = get_column_index("id", worksheet)
	name_column = get_column_index("name", worksheet)
	pickup_column = get_column_index("default pickup location", worksheet)

	# skip first row because it's the column header
	for row, value in enumerate(worksheet.col_values(phone_number_column)[1:], 2):
		if phonenumbers.parse(value, region) == phone_number:
			name = worksheet.cell(row, name_column).value
			id_number = worksheet.cell(row, id_column).value
			pickup_location = worksheet.cell(row, pickup_column).value
			return person.Person(name, id_number, phone_number, pickup_location)
	return None

def get_person_by_id(id_number):
	'''Given an id, returns the corresponding Person object. 
	None if they don't exist'''
	worksheet = SPREADSHEET.worksheet("People")

	phone_number_column = get_column_index("phone number", worksheet)
	id_column = get_column_index("id", worksheet)
	name_column = get_column_index("name", worksheet)
	pickup_column = get_column_index("default pickup location", worksheet)

	for row, value in enumerate(worksheet.col_values(id_column), 1):
		if value == str(id_number):
			name = worksheet.cell(row, name_column).value
			phone_number = worksheet.cell(row, phone_number_column).value
			pickup_location = worksheet.cell(row, pickup_column).value
			return person.Person(name, id_number, phone_number, pickup_location)
	return None

def next_id():
	'returns the id of the next Person to create'
	ids = list()
	worksheet = SPREADSHEET.worksheet("People")
	id_column_index = get_column_index("id", worksheet)
	for id_number in worksheet.col_values(id_column_index)[1:]:
		try:
			ids.append(int(id_number))
		except ValueError: # ignore the value if it can't be converted to an int.
			pass
	return max(ids) + 1

def get_column_index(column_name, worksheet):
	'''Given a column name, returns the index of that column in the spreadsheet.
	Returns None if it can't find that column.
	'''
	# assumes first row defines the columns
	for index, name in enumerate(worksheet.row_values(1), 1): 
		if name == column_name:
			return index
	return None

def get_empty_row(worksheet):
	'''Searches the first column of the spreadsheet and returns the first row 
	that is empty in that column'''
	for row, value in enumerate(worksheet.col_values(1), 1):
		if value == '':
			return row
	# this should never happen. I'm pretty sure google spreadsheets have no row limit
	return -1

def might_be_useful_later():
	# map column names to column indices
	column_indices = dict()
	columns = worksheet.row_values(1)

	for index, column_name in enumerate(columns, 1):
		if column_name != '': # there's weird behavior where columns are blank
			column_indices[column_name] = index

	for column_name, column_index in column_indices.items():
		print(column_name, ":", column_index)	