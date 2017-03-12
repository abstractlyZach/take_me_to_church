# gspread_utils.py

import gspread_connection

class Cell:
	def __init__(self, worksheet, row, column, data):
		self._worksheet = worksheet
		self._data = data
		self._row = row
		self._column = column

	def get(self):
		return self._data

	def change(self, new_data):
		self._data = new_data

	def get_row(self):
		return self._row

	def get_column(self):
		return self._column

	def commit(self):
		'''Commits the cell's data to the worksheet.'''
		self._worksheet.update_cell(self._row, self._column, self._data)

	def __str__(self):
		return "({}, {}): {}".format(self._row, self._column, self._data)


class Row(dict):
	def __init__(self, autocommit_on=False):
		self._autocommit_on = autocommit_on
		self._changed_cells = set() # set of names of changed cells
		super().__init__()

	def change(self, attribute, new_data):
		cell = self[attribute]
		cell.change(new_data)
		if self._autocommit_on:
			cell.commit()
		else:
			self._changed_cells.add(attribute)

	def commit(self):
		'''Commits the changes to the spreadsheet and removes the list
		of changes that need to be committed'''
		for i in range(len(self._changed_cells)):
			attribute = self._changed_cells.pop()
			cell = self[attribute]
			cell.commit()

	def get_types(self):
		return {attribute: type(cell.get()) for attribute, cell in self.items()}

	def print(self):
		for column_name, cell in self.items():
			print('{:>25}: {}'.format(column_name, cell.get()))


def clean_row(row):
	'''Takes in a list of strings and returns a new list with everything
	after the first empty string removed.'''
	to_return = []
	for data in row:
		if data == '':
			return to_return
		to_return.append(data)
	return to_return # just in case I ever get a row with no empty strings



class RideWorksheet:
	'''Object that handles high-level management of a Google worksheet.
	Assumes that there is a header row (row 1). 
	Assumes that the header ends on the first empty field in the header row.
	Assumes that the spreadsheet is totally filled out. (No blank spaces in the filled columns)
	Stops loading the worksheet when it reaches the first empty row.'''
	def __init__(self, spreadsheet, worksheet_name, autocommit_on=False):
		self._autocommit_on = autocommit_on
		self._worksheet = spreadsheet.worksheet(worksheet_name)
		# get the header (gspread starts on row 1)
		self._column_labels = clean_row(self._worksheet.row_values(1))
		self._rows = [] # a list of dictionaries. Each dictionary represents a row
		current_row_counter = 2 # start from row beneath the header
		while True:
			row_data = clean_row(self._worksheet.row_values(current_row_counter))
			# break loop on first empty row
			if row_data == []: # row is empty
				break 
			row_dict = self._build_row(row_data, current_row_counter)
			self._rows.append(row_dict)
			current_row_counter += 1

	def _build_row(self, row_data, row_number):
		'''Takes in a list of strings'''
		row_dict = Row(autocommit_on=self._autocommit_on)
		for column, data in enumerate(row_data):
			# change to column + 1 for google spreadsheet purposes
			cell = Cell(self._worksheet, row_number, column + 1, data)
			row_dict[self._column_labels[column]] = cell
		return row_dict

	def print(self, step_mode=False):
		print('{} entries in worksheet.'.format(len(self._rows)))
		for row in self._rows:
			for column_name, cell in row.items():
				print('{:>25}: {}'.format(column_name, cell.get()))
			print()
			if step_mode:
				input()

	def find(self, attribute, value, single_row=True):
		'''Returns the row(s) that have the value 
		in the given column.'''
		rows_to_return = []
		for row in self._rows:
			if row[attribute].get().lower() == value.lower():
				if single_row:
					return row
				else:
					rows_to_return.append(row)
		if single_row: # couldn't find a row
			return None
		else: # return the list of rows, empty or not
			return rows_to_return

	def find_all(self, attribute, value):
		return self.find(attribute, value, single_row=False)

	def commit(self):
		for row in self._rows:
			row.commit()


if __name__ == '__main__':
	import time
	start = time.time()
	spreadsheet = gspread_connection.connect()
	worksheet = RideWorksheet(spreadsheet, 'Coming 2017-02-17')
	end = time.time()
	worksheet.print()
	print("time elapsed: {:.2f} seconds".format(end - start))