from twilio.rest import TwilioRestClient

accountSID = 'AC083764f799fd93b589fe6680151a33fa'
auth_token = '0c48948a17761ea584b912c9c1b270ca'

twilio_client = TwilioRestClient(accountSID, auth_token)

my_twilio_number = '+16264363230'
my_cell_number = '+16263778839'
jonathan = '+18184703242'
stella = '+12133935454'

# message = twilio_client.messages.create(body='Mr. Watson - Come here - I want to see you.', 
# 			from_=my_twilio_number, to=my_cell_number)

body_str = 'TESTING 123 TESTING 123'
message = twilio_client.messages.create(body=body_str,
			from_=my_twilio_number, to=stella)

body_str = "respond to me!"
message = twilio_client.messages.create(body=body_str,
			from_=my_twilio_number, to=stella)