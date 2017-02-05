# get_info.py
# retrieves information from the google spreadsheet

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import person

# 1. go to https://console.developers.google.com/iam-admin/projects
# 2. enable drive API
# 3. go to Credentials > New Credentials > Service account key >
#           use defaults and it will download a json file
# 4. insert the downloaded json file for credentials here
# 5. create a google spreadsheet on your own account and "share" it with 
#        the email included in the json file


# Log into the google account and returns a spreadsheet object that allows
#     you to carry out operations on it
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name( \
	'GLMC Irvine Rides-ae48e51e1772.json', scope)
gc = gspread.authorize(credentials)
SPREADSHEET = gc.open('GLMC Rides')



def get_person_by_phone(phone_number):
	'''Given a phone number, returns the corresponding Person object. 
	None if they don't exist'''
	worksheet = SPREADSHEET.worksheet("People")

	phone_number_column = get_column_index("phone number", worksheet)
	id_column = get_column_index("id", worksheet)
	name_column = get_column_index("name", worksheet)
	pickup_column = get_column_index("default pickup location", worksheet)

	for row, value in enumerate(worksheet.col_values(phone_number_column), 1):
		if value == phone_number:
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


def get_column_index(column_name, worksheet):
	'''Given a column name, returns the index of that column in the spreadsheet.
	Returns None if it can't find that column.
	'''
	# assumes first row defines the columns
	for index, name in enumerate(worksheet.row_values(1), 1): 
		if name == column_name:
			return index
	return None


def might_be_useful_later():
	# map column names to column indices
	column_indices = dict()
	columns = worksheet.row_values(1)

	for index, column_name in enumerate(columns, 1):
		if column_name != '': # there's weird behavior where columns are blank
			column_indices[column_name] = index

	for column_name, column_index in column_indices.items():
		print(column_name, ":", column_index)	