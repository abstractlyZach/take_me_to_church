# first_contact.py

# initiates first contact for adding a new person to the system

import set_info
import get_info
import messages

def run(name, number, pickup=None):
	new_id = set_info.add_person(name, number, pickup)
	person = get_info.get_person_by_id(new_id)
	welcome_message = "Hi! I'm the GLMC Ride coordinator bot! "
	welcome_message += "Nice to meet you, {} :) ".format(person.get_name())
	welcome_message += "I'll be messaging you weekly to see if you're coming "
	welcome_message += "to GLMC, so make sure to save my number in your contacts! "
	welcome_message += "I'm just a bot, so if you have any big questions, make sure "
	welcome_message += "to contact Zach instead at (626) 377-8839. See ya later!"
	messages.send_message(person, welcome_message)
	chuck_norris_message = "oh also, if you text me the word 'chuck', I'll tell you a "
	chuck_norris_message += "Chuck Norris joke"
	messages.send_message(person, chuck_norris_message)

if __name__ == '__main__':
	action = ''
	print("Welcome to the PERSON ADDER. Use this to add people to the rides system!")
	print()
	while True:
		action = input("New Person... (Enter to continue, q to quit)")
		if action.lower() == 'q':
			break
		name = input("Name: ")
		phone = input("Phone number: ")
		run(name, phone)
	print("exiting PERSON ADDER.")