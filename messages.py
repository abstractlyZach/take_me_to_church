# messages.py

# this module handles sending messages to people

from twilio.rest import TwilioRestClient
import credentials
import get_info
import person

accountSID = credentials.TWILIO_ACCOUNT_SID
auth_token = credentials.TWILIO_AUTH_TOKEN

MY_PHONE = get_info.get_person_by_id(0).get_international_phone()
HEADER_SEPARATOR = '- -\n\n' 
# added dashes because twilio strips leading whitespace, so the newlines would be useless


def send_message(target, message):
	twilio_client = TwilioRestClient(accountSID, auth_token)
	if isinstance(target, person.Person):
		target_number = target.get_international_phone()
	else:
		target_number = target
	message = HEADER_SEPARATOR + message # separate the trial header from the message
	return twilio_client.messages.create(body=message,
			from_=MY_PHONE, to=target_number)

def message_everyone(message):
	twilio_client = TwilioRestClient(accountSID, auth_token)
	message = HEADER_SEPARATOR + message # separate the trial header from the message
	for id_ in range(get_info.next_id()): # loop through all ids
		person = get_info.get_person_by_id(id_)
		send_message(person, message)
