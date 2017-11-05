import os
from django.core.mail import send_mail
from django.conf import settings


def email(content):
    title = 'ON THIS DAY results'
    send_mail(
        title,
        content,
        settings.ADMIN_EMAIL_ADDRESS,
        [settings.EMAIL_ADDRESS]
    )
