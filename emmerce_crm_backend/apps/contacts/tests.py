from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from emmerce_crm_backend.apps.authentication.models import CustomUser as User
from emmerce_crm_backend.apps.contacts.models import Contact
from emmerce_crm_backend.apps.leads.models import Lead

import json

class ContactAPITestCase(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.lead = Lead.objects.create(name='Test Lead', owner=self.user)
        self.valid_payload = {
            'name': 'Test Contact',
            'phone': '1234567890',
            'email': 'test@example.com',
            'lead': self.lead.id
        }

    def test_create_contact(self):
        url = reverse('contacts:contact-list')
        response = self.client.post(url, data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_contacts(self):
        url = reverse('contacts:contact-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_contact_detail(self):
        contact = Contact.objects.create(name='Test Contact', phone='1234567890', email='test@example.com', lead=self.lead)
        url = reverse('contacts:contact-detail', args=[contact.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_contact(self):
        contact = Contact.objects.create(name='Test Contact', phone='1234567890', email='test@example.com', lead=self.lead)
        url = reverse('contacts:contact-detail', args=[contact.pk])
        updated_payload = {
            'name': 'Updated Contact',
            'phone': '0987654321',
            'email': 'updated@example.com',
            'lead': self.lead.id
        }
        response = self.client.put(url, data=json.dumps(updated_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_contact(self):
        contact = Contact.objects.create(name='Test Contact', phone='1234567890', email='test@example.com', lead=self.lead)
        contact.lead = self.lead  # Ensure lead is assigned correctly
        contact.save()
        url = reverse('contacts:contact-detail', args=[contact.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
