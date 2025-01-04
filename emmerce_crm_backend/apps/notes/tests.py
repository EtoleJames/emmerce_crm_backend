from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from emmerce_crm_backend.apps.authentication.models import CustomUser as User
from emmerce_crm_backend.apps.notes.models import Note
from emmerce_crm_backend.apps.contacts.models import Lead
import json

class NoteAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.lead = Lead.objects.create(name='Test Lead', email='lead@example.com', phone='1234567890', owner=self.user)
        self.valid_payload = {
            'content': 'Test Note Content',
            'lead': self.lead.id
        }

    def test_create_note(self):
        url = reverse('notes:note-list')
        response = self.client.post(url, data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_notes(self):
        url = reverse('notes:note-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_note_detail(self):
        note = Note.objects.create(content='Test Note Content', lead=self.lead)
        url = reverse('notes:note-detail', args=[note.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note(self):
        note = Note.objects.create(content='Test Note Content', lead=self.lead)
        url = reverse('notes:note-detail', args=[note.pk])
        updated_payload = {
            'content': 'Updated Note Content',
            'lead': self.lead.id
        }
        response = self.client.put(url, data=json.dumps(updated_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_note(self):
        note = Note.objects.create(content='Test Note Content', lead=self.lead)
        url = reverse('notes:note-detail', args=[note.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify note is deleted
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
