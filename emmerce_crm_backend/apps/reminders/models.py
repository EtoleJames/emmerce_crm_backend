from django.db import models
from emmerce_crm_backend.apps.leads.models import Lead

class Reminder(models.Model):
    lead = models.ForeignKey(Lead, related_name='reminders', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    remind_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reminder for {self.lead.name}"