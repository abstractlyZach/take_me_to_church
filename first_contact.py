from twilio.rest import TwilioRestClient
import get_info
import credentials

accountSID = credentials.TWILIO_ACCOUNT_SID
auth_token = credentials.TWILIO_AUTH_TOKEN

twilio_client = TwilioRestClient(accountSID, auth_token)

my_twilio_account = get_info.get_person_by_id(0)
zach = get_info.get_person_by_id(1)

body_str = 'TESTING 123 TESTING 123'
message = twilio_client.messages.create(body=body_str,
			from_=my_twilio_account.get_phone(), to='+1 626-377-8839')

body_str = "respond to me!"
message = twilio_client.messages.create(body=body_str,
			from_=my_twilio_account.get_phone(), to='+1 626-377-8839')