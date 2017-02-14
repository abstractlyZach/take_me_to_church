# jokes.py

import requests

def get_chuck_norris_joke():
	'Returns a joke from the Internet Chuck Norris Database'
	response = requests.get('http://api.icndb.com/jokes/random')
	data = response.json()
	joke = data['value']['joke']
	return joke