# handle_message.py

from nltk.tokenize import word_tokenize
import get_info
import jokes
import check_rides

DEFAULT_DEPARTURE_TIME = "7:00PM"
DATE = '2017-02-17'
DEPARTURE_TIME_MESSAGE = "Are you down to leave at the usual time ({})? " + \
	"If not, when do you want to leave?"
DEPARTURE_TIME_MESSAGE = DEPARTURE_TIME_MESSAGE.format(DEFAULT_DEPARTURE_TIME)

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
		person = get_info.get_person_by_phone(self._phone_number)
		if self._message.strip().lower() == 'password':
			return "Welcome to the club"
		elif self._message.strip().lower() == 'chuck':
			return jokes.get_chuck_norris_joke()
		elif tokens[0] == "yes":
			if not check_rides.coming_to_church(DATE, person.get_name()):
				check_rides.create_person(person.get_name())
				return "Got it! Are you down to drive people? (yes/no)"
			else:
				if check_rides.person_field_missing(DATE, person.get_name(), 'driver/rider'):
					# print("setting person as a driver!!!")
					check_rides.set_as_driver(DATE, person.get_name())
					# print("finished setting person as a driver!")
					return "Are you down to leave at the usual time ({})? If not, when do you want to leave?".format(DEFAULT_DEPARTURE_TIME)
				elif check_rides.person_field_missing(DATE, person.get_name(), 'departure time'):
					check_rides.set_default_departure_time(DATE, person.get_name())
					return "OK! you'll be leaving at the default time."
				else:
					self.unparsed_response()
					return ""

		elif tokens[0] == "no":
			if not check_rides.coming_to_church(DATE, person.get_name()):
				return "ok! Have a good week"
			else:
				if check_rides.person_field_missing(DATE, person.get_name(), 'driver/rider'):
					check_rides.set_as_rider(DATE, person.get_name())
					return "Are you down to leave at the usual time ({})? If not, when do you want to leave?".format(DEFAULT_DEPARTURE_TIME)
				else:
					self.unparsed_response()
					return ""

		else: # didn't send the secret password
			coming = check_rides.coming_to_church(DATE, person.get_name())
			if coming:
				got_driver_rider = not check_rides.person_field_missing(DATE, person.get_name(), 'driver/rider')
			if coming and got_driver_rider:
				check_rides.set_departure_time(DATE, person.get_name(), self._message)
				return "Got it! Message me a new time if you need to change your time"
			else:
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
		return "" # temporary placeholder before I add in more logic. makes sure I always return a string

	def unparsed_response(self):
		print('unparsed response.')
		print('idk where this should go. printing message:')
		print(self._message)
		 
