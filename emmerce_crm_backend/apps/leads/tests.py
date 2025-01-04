from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from emmerce_crm_backend.apps.authentication.models import CustomUser as User
from emmerce_crm_backend.apps.leads.models import Lead
import json

class LeadAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.valid_payload = {
            'name': 'Test Lead',
            'email': 'testlead@example.com',
            'phone': '1234567890',
            'owner': self.user.id
        }
    def test_create_lead(self):
        url = reverse('leads:lead-list')
        response = self.client.post(url, data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_leads(self):
        url = reverse('leads:lead-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lead_detail(self):
        lead = Lead.objects.create(name='Test Lead', owner=self.user)
        url = reverse('leads:lead-detail', args=[lead.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lead(self):
        lead = Lead.objects.create(name='Test Lead', owner=self.user)
        url = reverse('leads:lead-detail', args=[lead.pk])
        updated_payload = {
            'name': 'Updated Lead',
            'email': 'updatedlead@example.com',
            'phone': '0987654321',
            'owner': self.user.id
        }
        response = self.client.put(url, data=json.dumps(updated_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lead(self):
        lead = Lead.objects.create(name='Test Lead', email='testlead@example.com', phone='1234567890', owner=self.user)
        lead.save()
        url = reverse('leads:lead-detail', args=[lead.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify lead is deleted
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)