from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from app.models import TypeUser
from app.tests.utils import create_pack_noivo_for_tests


class AuthTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.register_url = '/api/auth/register/'
        self.login_url = '/api/auth/login/'
        self.logout_url = '/api/auth/logout/'
        self.user_url = '/api/auth/user/'
        self.reset_password_url = reverse('password_reset:reset-password-request')
        self.user_data = {
            'username': 'test_user',
            'email': 'testuser@test.com',
            'password': 'Admin123!',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'type': TypeUser.NOIVO
        }
        self.user, self.custom_user, self.noivo, self.evento = create_pack_noivo_for_tests()

    def test_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(pk=2).username, self.user_data['username'])

    def test_login(self):
        response = self.client.post(self.login_url, {
            'username': self.user.username,
            'password': '123456'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_retrieve_authenticated_user(self):
        response = self.client.post(self.login_url, {
            'username': self.user.username,
            'password': '123456'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        response = self.client.get(self.user_url, HTTP_AUTHORIZATION='Token ' + response.data['token'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_logout(self):
        response = self.client.post(self.login_url, {
            'username': self.user.username,
            'password': '123456'
        }, format='json')
        response = self.client.post(self.logout_url, HTTP_AUTHORIZATION='Token ' + response.data['token'])
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def test_reset_password(self):
    #     print(self.reset_password_url)
    #     response = self.client.post(self.reset_password_url, {'email': self.user_data['email']}, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
