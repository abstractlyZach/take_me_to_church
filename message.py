# message.py

# this module handles sending messages to people

from twilio.rest import TwilioRestClient
import credentials
import get_info
import person

accountSID = credentials.TWILIO_ACCOUNT_SID
auth_token = credentials.TWILIO_AUTH_TOKEN

MY_PHONE = get_info.get_person_by_id(0).get_international_phone()


def send_message(target, message):
	twilio_client = TwilioRestClient(accountSID, auth_token)
	if isinstance(target, person.Person):
		target_number = target.get_international_phone()
	else:
		target_number = target
	return twilio_client.messages.create(body=message,
			from_=MY_PHONE, to=target_number)