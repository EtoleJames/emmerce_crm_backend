from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class AuthenticationTests(APITestCase):
    def test_user_registration(self):
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpass123'}
        response = self.client.post('/api/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        data = {'email': 'test@example.com', 'password': 'testpass123'}
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_logout(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        refresh = RefreshToken.for_user(user)
        data = {'refresh': str(refresh)}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')
        response = self.client.post('/api/auth/logout/', data)
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)