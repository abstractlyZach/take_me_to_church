# handle_message.py

import nltk
from nltk.tokenize import word_tokenize
import get_info
import jokes
import check_rides

DEFAULT_DEPARTURE_TIME = "7:00PM"

nltk.download('punkt')

class MessageHandler:
	def __init__(self, message, session_counter, phone_number):
		# The message the server just received
		self._message = message 

		# How many times this person has sent a message in this session
		# Session times out after 4 hours
		self._session_counter = session_counter

		# Phone number of the person texting the server
		self._phone_number = phone_number

	def get_response(self):
		'''Returns a the appropriate response to a text message. Uses its object attributes
		to craft the response. Returns a string.
		'''
		tokens = word_tokenize(self._message)
		tokens = [token.lower() for token in tokens]
		if self._message.strip().lower() == 'password':
			return "Welcome to the club"
		elif self._message.strip().lower() == 'chuck':
			return jokes.get_chuck_norris_joke()
		elif tokens[0] == "yes":
			person = get_info.get_person_by_phone(self._phone_number)
			if not check_rides.coming_to_church('2017-02-17', person.get_name()):
				check_rides.create_person(person.get_name())
			else:
				print("duplicate response!")
		elif tokens[0] == "no":
			pass
		else: # didn't send the secret password
			sender = get_info.get_person_by_phone(self._phone_number)
			if sender == None:
				name = "stranger"
			else:
				name = sender.get_name()
			format_string = ("Hello {}. You have sent {} messages this session. "
				'You sent "{}". ')
			# if sender != None:
			# 	if sender.get_pickup_location() != None:
			# 		format_string += "I'll pick you up at {}!".format(sender.get_pickup_location())
			return format_string.format(name, self._session_counter, self._message)
		 
