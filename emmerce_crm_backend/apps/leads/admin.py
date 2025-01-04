from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'owner', 'created_at']
    search_fields = ['name', 'email', 'phone']