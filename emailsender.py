from flask import Flask, request, jsonify # type: ignore
from flask_mail import Mail, Message # type: ignore

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send', methods=['POST'])
def send_email():
    data = request.get_json()
    emails = data['emails']
    subject = data['subject']
    message = data['message']

    msg = Message(subject, sender='your-email@gmail.com', recipients=emails)
    msg.body = message

    mail.send(msg)
    return jsonify({'message': 'Emails sent successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
