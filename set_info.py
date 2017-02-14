# set_info.py

import person
import get_info
import gspread_connection
import phonenumbers

def add_person(name, number, pickup=None):
	'Add a person to the "People" worksheet. Returns their id number.'
	# connect to spreadsheet
	spreadsheet = gspread_connection.connect()
	worksheet = spreadsheet.worksheet('People')
	# get the column numbers
	phone_number_column = get_info.get_column_index("phone number", worksheet)
	id_column = get_info.get_column_index("id", worksheet)
	name_column = get_info.get_column_index("name", worksheet)
	pickup_column = get_info.get_column_index("default pickup location", worksheet)
	# get the id for the new person
	id_number = get_info.next_id()
	# parse and format phone number
	number = phonenumbers.parse(number, "US")
	number = phonenumbers.format_number(number, 
										phonenumbers.PhoneNumberFormat.NATIONAL)
	# find the next empty row in the worksheet
	row = get_info.get_empty_row(worksheet)
	# set the cells on the worksheet
	worksheet.update_cell(row, name_column, name)
	worksheet.update_cell(row, id_column, id_number)
	worksheet.update_cell(row, phone_number_column, number)
	worksheet.update_cell(row, pickup_column, pickup)
	return id_number
