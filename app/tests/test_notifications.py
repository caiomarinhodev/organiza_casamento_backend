from django.test import TestCase

from app.models import Task
from app.tests.utils import create_pack_noivo_for_tests
from rest_framework.test import APIClient


class EndpointsTestCase(TestCase):
    def setUp(self):
        self.user, self.custom_user, self.noivo, self.evento = create_pack_noivo_for_tests()
        self.client = APIClient()

    def test_notification_view(self):
        url = '/api/user/' + str(self.user.pk) + '/notifications/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print(response.data)
        self.assertEqual(len(response.data), 1)

    def test_notification_mark_all_read(self):
        url = '/api/user/' + str(self.user.pk) + '/notifications/mark_all_read/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

        notifications = self.custom_user.notification_set.filter(is_read=True)
        self.assertEqual(len(notifications), 1)

    def test_notification_mark_read(self):
        notification = self.custom_user.notification_set.all().first()
        notification.is_read = False
        notification.save()

        url = '/api/user/' + str(self.user.pk) + '/notifications/' + str(notification.pk) + '/mark_read/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

        notification = self.custom_user.notification_set.get(pk=1)
        self.assertTrue(notification.is_read)
