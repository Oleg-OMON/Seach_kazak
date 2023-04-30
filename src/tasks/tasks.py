from email.message import EmailMessage
from celery import Celery
from config import MY_APP_USER, MY_APP_PASSWORD
import smtplib


SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465


celery = Celery('tasks', broker='redis://localhost:6379')


def get_email(username: str):
    email = EmailMessage()
    email['Subject'] = 'Добро пожаловать'
    email['From'] = MY_APP_USER
    email['To'] = MY_APP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, Добро пожаловать) 😊</h1>'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_welcome_email(username: str):
    email = get_email(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(MY_APP_USER, MY_APP_PASSWORD)
        server.send_message(email)
