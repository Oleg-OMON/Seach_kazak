import smtplib
from email.message import EmailMessage

from celery import Celery

from src.config import MY_APP_USER, MY_APP_PASSWORD

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465


celery = Celery('tasks', broker='redis:localhost:6379')


def get_email(username: str):
    email = EmailMessage()
    email['Subject'] = 'Добро пожаловать'
    email['From'] = MY_APP_USER
    email['To'] = MY_APP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
        '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
        '-mobile-free-vector.jpg" width="600">'
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
