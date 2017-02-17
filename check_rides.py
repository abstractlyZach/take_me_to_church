# check_rides.py

import get_info
import gspread_connection

def create_person(name):
	spreadsheet = gspread_connection.connect()
	worksheet = spreadsheet.worksheet('Coming 2017-02-17')
	empty_row = get_info.get_empty_row(worksheet)
	worksheet.update_cell(empty_row, 1, name)
	worksheet.update_cell(empty_row, 2, "unknown")
	worksheet.update_cell(empty_row, 3, "unknown")

def coming_to_church(date, name):
	'Returns true/false depending on if the person is coming this week'
	spreadsheet = gspread_connection.connect()
	worksheet = spreadsheet.worksheet('Coming {}'.format(date))
	name_column = get_info.get_column_index('name', worksheet)
	return name in worksheet.col_values(name_column)

def person_field_missing(date, name, field):
	'Returns true if the field has "unknown" in it'
	assert coming_to_church(date, name)
	spreadsheet = gspread_connection.connect()
	worksheet = spreadsheet.worksheet('Coming {}'.format(date))
	field_column = get_info.get_column_index(field, worksheet)
	person_row = get_person_row(date, name)
	return worksheet.cell(person_row, field_column).value == 'unknown'

def set_as_driver(date, name):
	'Sets a person as driver for the date'
	assert coming_to_church(date, name)
	spreadsheet = gspread_connection.connect()
	worksheet = spreadsheet.worksheet('Coming {}'.format(date))
	field_column = get_info.get_column_index('driver/rider', worksheet)
	person_row = get_person_row(date, name)
	worksheet.update_cell(person_row, field_column, 'driver')

def set_as_rider(date, name):
	'Sets a person as rider for the date'
	assert coming_to_church(date, name)
	spreadsheet = gspread_connection.connect()
	worksheet = spreadsheet.worksheet('Coming {}'.format(date))
	field_column = get_info.get_column_index('driver/rider', worksheet)
	person_row = get_person_row(date, name)
	worksheet.update_cell(person_row, field_column, 'rider')

def set_default_departure_time(date, name):
	set_departure_time(date, name, 'default')

def set_departure_time(date, name, time):
	assert coming_to_church(date, name)
	spreadsheet = gspread_connection.connect()
	worksheet = spreadsheet.worksheet('Coming {}'.format(date))
	time_column = get_info.get_column_index('departure time', worksheet)
	person_row = get_person_row(date, name)
	worksheet.update_cell(person_row, time_column, time)

def get_person_row(date, name):
	"Gets the row for a person. Returns -1 if they're not coming this week"
	if not coming_to_church(date, name):
		return -1
	else:
		spreadsheet = gspread_connection.connect()
		worksheet = spreadsheet.worksheet('Coming {}'.format(date))
		name_column = get_info.get_column_index('name', worksheet)
		for row, person_name in enumerate(worksheet.col_values(name_column), 1):
			if name == person_name:
				return row
