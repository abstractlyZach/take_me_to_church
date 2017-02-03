# handle_message.py
import nltk
import get_info

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
		if self._message == 'password':
			return "Welcome to the club"
		else: # didn't send the secret password
			sender = get_info.get_person_by_number(self._phone_number)
			if sender == None:
				name = "stranger"
			else:
				name = sender.get_name()
			format_string = ("Hello {}. You have sent {} messages this session. "
				'You sent "{}"')
			return format_string.format(name, self._session_counter, self._message)
		 
