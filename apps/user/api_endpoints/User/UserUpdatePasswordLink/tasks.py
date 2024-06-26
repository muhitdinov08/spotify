from django.core.mail import send_mail
import os
from dotenv import load_dotenv
from celery import app

load_dotenv()


@app.Celery
def send_email(subject, message, recepient_list):
    user_email = os.getenv("EMAIL_HOST_USER")
    send_mail(subject, message, user_email, recepient_list)
