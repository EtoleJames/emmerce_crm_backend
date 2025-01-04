from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Lead

User = get_user_model()

class LeadTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(self.refresh.access_token)}')
        self.lead_data = {'name': 'Test Lead', 'email': 'lead@example.com', 'phone': '1234567890'}

    def test_create_lead(self):
        response = self.client.post('/api/leads/', self.lead_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_leads(self):
        Lead.objects.create(owner=self.user, **self.lead_data)
        response = self.client.get('/api/leads/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_lead(self):
        lead = Lead.objects.create(owner=self.user, **self.lead_data)
        update_data = {'name': 'Updated Lead', 'email': 'updated@example.com', 'phone': '0987654321'}
        response = self.client.put(f'/api/leads/{lead.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Lead')

    def test_delete_lead(self):
        lead = Lead.objects.create(owner=self.user, **self.lead_data)
        response = self.client.delete(f'/api/leads/{lead.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)