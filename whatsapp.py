
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    number = request.form['number']
    # Here you can add code to send OTP to the user's phone number
    # For example, using Twilio API:
    # from twilio.rest import Client
    # account_sid = 'your_account_sid'
    # auth_token = 'your_auth_token'
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body='Your OTP is 123456',
    #     from_='your_twilio_number',
    #     to=number
    # )
    return redirect(url_for('otp', number=number))

@app.route('/otp/<number>', methods=['GET', 'POST'])
def otp(number):
    if request.method == 'POST':
        otp = request.form['otp']
        # Here you can add code to verify the OTP entered by the user
        # For example, using a database or an external API
        return redirect(url_for('offline'))
    return render_template('otp.html', number=number)

@app.route('/offline')
def offline():
    return render_template('offline.html')


if __name__ == '__main__':
    app.run(debug=True)