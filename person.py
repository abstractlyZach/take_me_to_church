# person.py

import phonenumbers
import get_info
import gspread_connection

class Person:
	'''Class for representing a person. Riders and Drivers inherit from Person.
		Handles person things, like phone number, housing community, name, etc.'''
	def __init__(self, name, id_number, phone, pickup_location=None):
		'''Initializes a user with a name and id. Other fields are optional and 
			can be added later.'''
		self._name = name
		self._id = id_number
		self.set_phone(phone)
		self._pickup_location = pickup_location

	def get_name(self):
		return self._name

	def get_id(self):
		return self._id

	def rename(self, name):
		self._name = name

	def set_phone(self, number, region='US'):
		if not isinstance(number, phonenumbers.PhoneNumber):
			self._phone = phonenumbers.parse(number, 'US')
		else:
			self._phone = number

	def get_phone(self):
		return self._phone

	def get_international_phone(self):
		return phonenumbers.format_number(self._phone, 
										phonenumbers.PhoneNumberFormat.INTERNATIONAL)

	def get_national_phone(self):
		return phonenumbers.format_number(self._phone, 
										phonenumbers.PhoneNumberFormat.NATIONAL)

	def set_pickup_location(self, pickup_location):
		self._pickup_location = pickup_location

	def get_pickup_location(self):
		return self._pickup_location

	def write_to_spreadsheet(self):
		'''Writes this person's info to the spreadsheet. Returns exception if
		they have a duplicate id'''
		SPREADSHEET = gspread_connection.connect()
		worksheet = SPREADSHEET.worksheet('People')
		id_column_index = get_info.get_column_index('id', worksheet)
		# get list of ids and strip the header on the spreadsheet
		ids = list()
		for id_number in worksheet.col_values(id_column_index)[1:]:
			try:
				ids.append(int(id_number))
			except ValueError: # ignore the value if it can't be converted to an int.
				pass
		if self._id in ids:
			raise Exception("There is a person on the spreadsheet who has the same ID!")
		empty_row = get_info.get_empty_row(worksheet)
		name_column_index = get_info.get_column_index('name', worksheet)
		pickup_column_index = get_info.get_column_index('default pickup location', worksheet)
		phone_number_column_index = get_info.get_column_index('phone number', worksheet)
		worksheet.update_cell(empty_row, id_column_index, self.get_id())
		worksheet.update_cell(empty_row, name_column_index, self.get_name())
		worksheet.update_cell(empty_row, pickup_column_index, self.get_pickup_location())
		worksheet.update_cell(empty_row, phone_number_column_index, self.get_national_phone())

	def __str__(self):
		indent = '    '
		to_return = '{}:\n'.format(self.get_name())
		to_return += '{}{:16}: {}\n'.format(indent, 'id', self.get_id())	
		to_return += '{}{:16}: {}\n'.format(indent, 'phone', self.get_national_phone())
		to_return += '{}{:16}: {}\n'.format(indent, 'pickup location', self.get_pickup_location())
		return to_return

