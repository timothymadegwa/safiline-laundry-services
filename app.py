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
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        pickup_date = request.form['pickup-date']
        delivery_date = request.form['delivery-date']
        residence = request.form['residence']
        try:
            care = request.form['care']
        except:
            care = "NONE"
        try:
            delivery = request.form['delivery']
        except:
            delivery = "NONE"
        
        email_message = f"""Hello, there has been a booking on the Safiline Website by {name} with the email address {email} and phone number {phone}.
        Pickup date is {pickup_date} and the delivery date is {delivery_date}. 
        The client's residence is {residence}.
        Care Instructions -> {care}
        Delivery Instructions -> {delivery}.
        Thank you!
        """
        msg = Message(subject="Hello", sender=email_sender, recipients=["timothymadegwa@gmail.com"])
        msg.body = email_message
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