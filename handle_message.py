# handle_message.py

class MessageHandler:
	def __init__(self, message, session_counter, name):
		# The message the server just received
		self._message = message 

		# How many times this person has sent a message in this session
		# Session times out after 4 hours
		self._session_counter = session_counter

		# Name of the person texting the server
		self._name = name

	def get_response(self):
		format_string = ("Hello {}. You have sent {} messages this session. "
			'You sent "{}"')
		# return format_string.format(self._name, self._session_counter, self._message)
		return "deploy.sh works!!!"