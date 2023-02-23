from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


app = Flask(__name__)
email_sender = os.getenv("EMAIL_HOST_USER")
app.config["MAIL_SERVER"] = os.getenv("EMAIL_HOST")
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = email_sender
app.config["MAIL_PASSWORD"] = os.getenv("EMAIL_HOST_PASSWORD")
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

mail = Mail(app)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        msg = Message(subject="Hello", sender=email_sender, recipients=["timothymadegwa@gmail.com"])
        msg.body = "Test Email"
        mail.send(msg)
        return "sent"

    return render_template('index.html')

@app.route('/send_mail')
def send_mail():
    msg = Message(subject="Hello", sender=email_sender, recipients=["timothymadegwa@gmail.com"])
    msg.body = "Test Email"
    mail.send(msg)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)