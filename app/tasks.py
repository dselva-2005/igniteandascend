# app_name/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task

def send_custom_email(subject, message, recipient_list, from_email=None, html_message=None):
    """
    Sends an email using Django's send_mail function.
    
    Args:
        subject (str): Subject of the email.
        message (str): Plain text version of the email.
        recipient_list (list): List of recipient email addresses.
        from_email (str, optional): Defaults to settings.DEFAULT_FROM_EMAIL.
        html_message (str, optional): HTML version of the email body.

    Returns:
        int: Number of successfully delivered messages (0 or 1).
    """
    return send_mail(
        subject,
        message,
        from_email or settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
        html_message=html_message,
    )

