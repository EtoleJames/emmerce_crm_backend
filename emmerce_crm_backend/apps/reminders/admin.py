from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['id', 'lead', 'remind_at', 'created_at', 'updated_at']
    search_fields = ['lead__name', 'message']