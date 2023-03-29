from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class AuthTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('knox-logout')
        self.user_url = reverse('user')
        self.reset_password_url = reverse('password_reset:reset-password-request')
        self.user_data = {
            'username': 'test_user',
            'email': 'testuser@test.com',
            'password': 'test_password',
        }
        self.login_data = {
            'username': 'test_user',
            'password': 'test_password'
        }

    def test_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get().username, self.user_data['username'])

    def test_login(self):
        get_user_model().objects.create_user(**self.user_data)
        response = self.client.post(self.login_url, self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_retrieve_authenticated_user(self):
        get_user_model().objects.create_user(**self.user_data)
        response = self.client.post(self.login_url, self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        response = self.client.get(self.user_url, HTTP_AUTHORIZATION='Token ' + response.data['token'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user_data['username'])

    def test_logout(self):
        get_user_model().objects.create_user(**self.user_data)
        response = self.client.post(self.login_url, self.login_data, format='json')
        response = self.client.post(self.logout_url, HTTP_AUTHORIZATION='Token ' + response.data['token'])
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def test_reset_password(self):
    #     print(self.reset_password_url)
    #     response = self.client.post(self.reset_password_url, {'email': self.user_data['email']}, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
