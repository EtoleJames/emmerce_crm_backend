from django.db import models
from emmerce_crm_backend.apps.leads.models import Lead

class Contact(models.Model):
    lead = models.ForeignKey(Lead, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name