# run.py
# This is the code that runs on the heroku server.

from flask import Flask, request, redirect, session
import twilio.twiml
import handle_message
import credentials


# The session object makes use of a secret key.
SECRET_KEY = credentials.FLASK_SECRET_KEY
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/", methods=['GET', 'POST'])
def respond():
    session_counter = session.get('counter', 0)
    # increment the counter
    session_counter += 1
    # Save the new counter value in the session
    session['counter'] = session_counter

    # store the number that sent the message
    from_number = request.values.get('From')

    # Get the received message
    message = request.form['Body']
    
    message_handler = handle_message.MessageHandler(message, session_counter, from_number)
    response_str = message_handler.get_response()

    resp = twilio.twiml.Response()
    resp.sms('\n\n' + response_str) # separates the trial header from the message

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
