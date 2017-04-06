from flask import Flask
from flask_mail import Mail
from flask_mail import Message

from security import pw

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'ursa.uberspace.de'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = app.debug
app.config['MAIL_USERNAME'] = 'hpfs@ursa.uberspace.de'
app.config['MAIL_PASSWORD'] = pw
app.config['MAIL_DEFAULT_SENDER'] = None
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPPRESS_SEND'] = app.testing
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)


@app.route("/")
def index():
    msg = Message("Hello",
    	body='Ich möchte bitte einen Termin.',
                  sender="homepage@heilpraktiker-frank-schneider.de",
                  recipients=["hpfs@ursa.uberspace.de"])
    mail.send(msg)
    return "Email wurde gesendet"

if __name__ == '__main__':
    app.run()
