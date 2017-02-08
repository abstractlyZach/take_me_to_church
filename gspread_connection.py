# gspread_connection.py
# Handles connection with google spreadsheets.


import gspread
from oauth2client.service_account import ServiceAccountCredentials

GOOGLE_CREDENTIALS_JSON = 'GLMC Irvine Rides-ae48e51e1772.json'
SCOPE = ['https://spreadsheets.google.com/feeds']


def connect(spreadsheet_name='GLMC Rides'):
	'''Log into the google account and returns a spreadsheet object that allows
     you to carry out operations on it '''
	credentials = ServiceAccountCredentials.from_json_keyfile_name( \
		GOOGLE_CREDENTIALS_JSON, SCOPE)
	gc = gspread.authorize(credentials)
	spreadsheet = gc.open(spreadsheet_name)
	return spreadsheet