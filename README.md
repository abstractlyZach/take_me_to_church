#Project Take Me To Church
Ride coordinators have a lot to think about:
* Am I aware of every person who wants a ride to church this week? 
* Did I coordinate details with drivers? 
* _Did I forget anyone?!_ (lol)  
* Do the drivers have the contact information and pickup information for all of their passengers?
* Who's leaving early? 
* Do I have enough drivers? Should I reach out to the church community to find more drivers to help? 
* How do I send a notification to everyone so they know if anything changes? 

This project aims to alleviate those problems and take care of the tedious work so that rides coordinators can focus on what they're good at: coordinating.

##Implementation
Technologies:
* Google spreadsheets 
  * http://sheets.google.com
  * stores information for riders and drivers
  * allows coordinator to get an overview of the rides situation
* Python
  * http://python.org
  * primary programming language for this project
* gspread 
  * http://github.com/burnash/gspread
  * allows Python to talk to Google spreadsheets
* Twilio 
  * http://twilio.com
  * SMS service for sending and receiving text messages
* Heroku 
  * http://heroku.com
  * hosts a server so that Twilio can ask it for a response to send back as a text message
* flask
  * http://flask.pocoo.org/
  * python server


##Sample Interactions
###Weekly Message





Make sure to install Twilio on your machine with
`pip install twilio`
on the command line

install gunicorn and flask. why do we need both? BEATS ME
