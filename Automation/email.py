import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def send_raise_email():
    sender_email = "your_email@example.com"
    receiver_email = "boss_email@example.com"
    password = "your_email_password"

    subject = "Request for Raise"
    body = """Hi Boss,

    It's been three months since our last conversation, and I'd like to revisit our discussion about my compensation.

    Best,
    Your Name"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

    print("Email sent to boss!")

# Run the script once every 3 months
while True:
    send_raise_email()
    time.sleep(60 * 60 * 24 * 90)  # Sleep for 3 months
