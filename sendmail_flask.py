from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure email settings for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'stoneshq20@gmail.com'  # Replace with your Gmail email
app.config['MAIL_PASSWORD'] = 'dvysrkgxubvykvbp' 
mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        data = request.json

        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        subject = data.get('subject')

        if name and email and message:
            subject = subject
            sender = 'stoneshq20@gmail.com'
            recipients = [email]

            msg = Message(subject=subject, sender=sender, recipients=recipients)
            msg.body = f"Name: {name}\nEmail: {email}\n\nSubject:\n{subject}\nMessage:\n{message}"

            try:
                mail.send(msg)
                response = {'message': 'Email sent successfully'}
                return jsonify(response), 200
            except Exception as e:
                response = {'message': 'An error occurred. Please try again later'}
                return jsonify(response), 500
        else:
            response = {'message': 'Missing required data'}
            return jsonify(response), 400
            


if __name__ == '__main__':
    app.run()

if __name__ == '__main__':
    app.run(debug=True)

