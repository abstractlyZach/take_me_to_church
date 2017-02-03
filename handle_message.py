# handle_message.py
import nltk

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
		format_string = ("Hello {}. You have sent {} messages this session. "
			'You sent "{}"')
		return format_string.format(self._phone_number, self._session_counter, self._message)
		 
