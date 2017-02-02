# group.py

import enum
import person

class Strength(enum.Enum):
	weak = 0
	medium = 1
	strong = 2
	required = 3


class Group:
	'''
	Implements constraints for people who want to/need to stick together.
	'''
	def __init__(self, strength, *args):
		self._members = set()
		if not isinstance(strength, Strength):
			raise Exception("Did not use a strength from the Strength enum.")
		self._strength = strength
		# Groups should be initialized with 2 or more people.
		if len(args) < 2:
			raise Exception("Tried to create a group with less than 2 people.")
		for member in args:
			if not isinstance(member, person.Person):
				raise Exception("Tried to create a group with a non-Person member.")
			else:
				self._members.add(person)

	def get_size(self):
		return len(self._members)

	def get_members(self):
		return self._members

	def add(self, new_member):
		'''Adds a new Person to the group as a member.'''
		self._members.add(new_member)

	def remove(self, member_to_remove):
		'''Removes a Person from the group.'''
		self._members.remove(member_to_remove)

	def get_strength(self):
		return self._strength

	def get_pickup_locations(self):
		'''Returns a set of the pickup locations for this group.'''
		return {member.get_pickup_location}

	def get_names(self):
		'''Returns a list of names of the group members.'''
		return [member.get_name() for member in self._members]

	def get_numbers(self):
		'''Returns a list of the phone numbers for the group.'''
		return [member.get_phone() for member in self._members]

	