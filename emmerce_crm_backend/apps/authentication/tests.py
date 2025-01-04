from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from faker import Faker
import factory
import json
from emmerce_crm_backend.apps.authentication.models import CustomUser

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.LazyAttribute(lambda _: fake.user_name())
    email = factory.LazyAttribute(lambda _: fake.email())
    phone = factory.LazyAttribute(lambda _: fake.phone_number())
    password = factory.PostGenerationMethodCall('set_password', 'StrongPass123!')


class AuthenticationTests(APITestCase):
    def setUp(self):
        # Set up client and endpoints
        self.client = APIClient()
        self.register_url = reverse('authentication:register')
        self.login_url = reverse('authentication:login')
        self.logout_url = reverse('authentication:logout')
        self.user = UserFactory()

    # Test User Registration
    def test_register_user(self):
        data = {
            "username": fake.user_name(),
            "email": fake.email(),
            "password": "StrongPass123!",
            "password2": "StrongPass123!",
            "phone": fake.phone_number()
        }

        response = self.client.post(self.register_url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])

    # Test Login
    def test_login_user(self):
        data = {"email": self.user.email, "password": "StrongPass123!"}
        response = self.client.post(self.login_url,json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    #Test Logout
    def test_logout_user(self):
    # Authenticate user
        data = {"email": str(self.user.email), "password": "StrongPass123!"}
        login_response = self.client.post(
            self.login_url, json.dumps(data), content_type='application/json'
        )

        # Extract tokens
        access_token = login_response.data['access']
        refresh_token = login_response.data['refresh']

        # Set Authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # Test logout endpoint
        response = self.client.post(
            self.logout_url, json.dumps({"refresh": refresh_token}), content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
