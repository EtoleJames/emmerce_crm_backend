from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from emmerce_crm_backend.apps.leads.models import Lead
from .models import Note

User = get_user_model()
class NoteTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}')
        self.lead = Lead.objects.create(owner=self.user, name='Lead 1', email='lead1@example.com', phone='1234567890')
        self.note_data = {'lead': self.lead.id, 'content': 'Test note content'}

    def test_create_note(self):
        response = self.client.post('/api/notes/', self.note_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_notes(self):
        Note.objects.create(lead=self.lead, **self.note_data)
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_note(self):
        note = Note.objects.create(lead=self.lead, **self.note_data)
        update_data = {'lead': self.lead.id, 'content': 'Updated note content'}
        response = self.client.put(f'/api/notes/{note.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], 'Updated note content')

    def test_delete_note(self):
        note = Note.objects.create(lead=self.lead, **self.note_data)
        response = self.client.delete(f'/api/notes/{note.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)