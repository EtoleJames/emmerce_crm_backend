from celery import shared_task
from django.core.mail import send_mail
from .models import Reminder
from datetime import datetime

@shared_task
def send_reminder_email():
    reminders = Reminder.objects.filter(remind_at__lte=datetime.now())
    for reminder in reminders:
        send_mail(
            'Reminder Notification',
            reminder.message,
            'from@emmerce-mini-crm.com',
            [reminder.lead.owner.email],
            fail_silently=False,
        )