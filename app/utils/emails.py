from os import environ
from flask_mail import Message
from app import mail


def send_email(subject, template, recipients):
    msg = Message(
        subject=subject,
        recipients=recipients
    )
    msg.html = template
    mail.send(msg)
