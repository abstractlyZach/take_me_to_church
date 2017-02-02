# person.py

class Person:
	'''Class for representing a person. Riders and Drivers inherit from Person.
		Handles person things, like phone number, housing community, name, etc.'''
	def __init__(self, name, id_number, phone=None, pickup_location=None):
		'''Initializes a user with a name and id. Other fields are optional and 
			can be added later.'''
		self._name = name
		self._id = id_number


	def get_name(self):
		return self._name

	def get_id(self):
		return self._id

	def rename(self, name):
		self._name = name

	def set_phone(self, number):
		self._phone = number

	def get_phone(self):
		return self._phone

	def set_pickup_location(self, pickup_location):
		self._pickup_location = pickup_location

	def get_pickup_location(self):
		return self._pickup_location

