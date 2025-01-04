from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from emmerce_crm_backend.apps.authentication.models import CustomUser as User
from emmerce_crm_backend.apps.reminders.models import Reminder
from emmerce_crm_backend.apps.contacts.models import Lead
from emmerce_crm_backend.apps.notes.models import Note
from emmerce_crm_backend.apps.reminders.tasks import send_reminder_email
from django.utils.timezone import now, timedelta
import json

class ReminderAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.lead = Lead.objects.create(name='Test Lead', email='lead@example.com', phone='1234567890', owner=self.user)
        self.note = Note.objects.create(content='Test Note Content', lead=self.lead)
        self.valid_payload = {
            'message': 'Test Reminder Message',
            'remind_at': '2025-01-04T10:00:00Z',
            'note': self.note.id,
            'lead': self.lead.id
        }

    def test_create_reminder(self):
        url = reverse('reminders:reminder-list')
        response = self.client.post(url, data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reminders(self):
        url = reverse('reminders:reminder-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reminder_detail(self):
        reminder = Reminder.objects.create(
            message='This is a test reminder.',
            remind_at=now() + timedelta(days=1),
            lead=self.lead
        )
        reminder.save()
        url = reverse('reminders:reminder-detail', args=[reminder.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_reminder(self):
        reminder = Reminder.objects.create(
            message='This is a test reminder.',
            remind_at=now() + timedelta(days=1),
            lead=self.lead
        )
        url = reverse('reminders:reminder-detail', args=[reminder.pk])
        updated_payload = {
            'message': 'Updated description.',
            'remind_at': (now() + timedelta(days=2)).isoformat(),
            'lead': self.lead.id
        }
        response = self.client.put(url, data=json.dumps(updated_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_reminder(self):
        reminder = Reminder.objects.create(
            message='This is a test reminder.',
            remind_at=now() + timedelta(days=1),
            lead=self.lead
        )
        url = reverse('reminders:reminder-detail', args=[reminder.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify reminder is deleted
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_celery_task_reminder(self):
        reminder = Reminder.objects.create(message='Test Reminder Message', remind_at='2025-01-04T10:00:00Z', lead=self.lead)
        self.assertEqual(reminder.message, 'Test Reminder Message')

