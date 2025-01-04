from django.db import models
from emmerce_crm_backend.apps.leads.models import Lead

class Note(models.Model):
    lead = models.ForeignKey(Lead, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note for {self.lead.name}"