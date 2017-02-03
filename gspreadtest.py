import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 1. go to https://console.developers.google.com/iam-admin/projects
# 2. enable drive API
# 3. go to Credentials > New Credentials > Service account key >
#           use defaults and it will download a json file
# 4. insert the downloaded json file for credentials here
# 5. create a google spreadsheet on your own account and "share" it with 
#        the email included in the json file

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name( \
	'GLMC Irvine Rides-ae48e51e1772.json', scope)

gc = gspread.authorize(credentials)

sh = gc.open('GLMC Rides') # <-- Look ma, no keys!

worksheet = sh.get_worksheet(0)

# map column names to column indices
column_indices = dict()
columns = worksheet.row_values(1)
for index, column_name in enumerate(columns, 1):
	if column_name != '': # there's weird behavior where columns are blank
		column_indices[column_name] = index

for column_name, column_index in column_indices.items():
	print(column_name, ":", column_index)


