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

# Try adding your own number to this list!
callers = {
    "+16263778839": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond with the number of text messages sent between two parties."""

    session_counter = session.get('counter', 0)
    # increment the counter
    session_counter += 1
    # Save the new counter value in the session
    session['counter'] = session_counter

    # store the number that sent the message
    from_number = request.values.get('From')
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Monkey"

    # Get the received message
    message = request.form['Body']
    
    message_handler = handle_message.MessageHandler(message, session_counter, name)
    response_str = message_handler.get_response()

    resp = twilio.twiml.Response()
    resp.sms(response_str)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
