from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from emmerce_crm_backend.apps.leads.models import Lead
from .models import Contact

User = get_user_model()

class ContactTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}')
        self.lead = Lead.objects.create(owner=self.user, name='Lead 1', email='lead1@example.com', phone='1234567890')
        self.contact_data = {'lead': self.lead.id, 'name': 'Test Contact', 'email': 'contact@example.com', 'phone': '1234567890'}

    def test_create_contact(self):
        response = self.client.post('/api/contacts/', self.contact_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_contacts(self):
        Contact.objects.create(lead=self.lead, **self.contact_data)
        response = self.client.get('/api/contacts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_contact(self):
        contact = Contact.objects.create(lead=self.lead, **self.contact_data)
        update_data = {'lead': self.lead.id, 'name': 'Updated Contact', 'email': 'updated@example.com', 'phone': '0987654321'}
        response = self.client.put(f'/api/contacts/{contact.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Contact')

    def test_delete_contact(self):
        contact = Contact.objects.create(lead=self.lead, **self.contact_data)
        response = self.client.delete(f'/api/contacts/{contact.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)