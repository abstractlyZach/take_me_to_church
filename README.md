#Project: Take Me To Church
Ride coordinators have a lot to think about.
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

The system will automatically send text messages to everyone to gather ride information. This ride information will be maintained in a Google spreadsheet so that the coordinator can easily look at the situation. If the coordinator needs to make changes, he just needs to make edits to the spreadsheet and then send a text to the system, which will send out texts to everyone with the updated information.

##Sample Interactions
###Weekly Message
```
> Hi! Are you coming to church this week?

  < Yes

> Will you be able to leave at the usual time (11:45AM)?

  < Yes

> Pick you up at your usual spot? (Parking lot near dining commons)

  < No

> Where do you want to be picked up?

  < Flagpoles

> Cool. I'll text you back when rides are all set up

some time later...

> You'll be going to church with Bob! His phone number is (123) 456-7890 and he'll pick you up 
      around 11:45AM (normal time) on Sunday
```

###Driver Message
```
> Hi! Are you coming to church this week?

  < Yes

> Are you down to drive people?

  < Yes

> Great! Will you be leaving at the usual time (11:45AM)?

  < Yes

> Cool. I'll text you back when rides are all set up

some time later...

> Can you please pick up:
 Joe: Mesa Court Lot 15 
   (213) 911-9111
   
 Sally: 1 Campus Drive, Irvine CA 92617
   (XXX) XXX-XXXX
...
around 11:45AM (normal time)
```

###First Interaction
```
> Hello! I'm the GLMC ride coordinator bot. I'll be contacting you about rides from now on! 
   I'm just a bot, so if you have any big questions, contact Jessica at (XXX) XXX-XXX. Will you be 
   ready to leave for GLMC college group at 7:15PM on Friday?

  < Yes

> Where can you be picked up?

  < From my workplace, 1234 Example Rd., Los Angeles CA

> Awesome. Did someone specific invite you to GLMC? I'll try to place you in his/her car

  < Anna

> Great! I'll try to put you in Anna's car. I'll contact you again soon when rides are set up

some time later...

> Your ride on Friday will be with Thomas. He's driving a silver Honda Civic with license plate "1ABC234". 
   He'll pick you up at "your workplace" around 7:15PM. If you need to contact him, his 
   number is (XXX) XXX-XXXX.
```

###How to install on your own machine


Make sure to install Twilio on your machine with
`pip install twilio`
on the command line

install gunicorn and flask. why do we need both? BEATS ME

__more to come. still writing this part__
