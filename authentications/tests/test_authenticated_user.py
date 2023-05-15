from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.tests.utils import create_pack_noivo_for_tests

User = get_user_model()


class TestRetrieveAuthenticatedUser(APITestCase):

    def setUp(self):
        self.url = reverse('user')
        self.user, self.custom_user, self.noivo, self.evento = create_pack_noivo_for_tests()

    def test_retrieve_authenticated_user_requires_authentication(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_authenticated_user_returns_user_info(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['email'], self.user.email)
