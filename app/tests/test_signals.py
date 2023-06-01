from django.test import TestCase

from app.models import Task, Notification, Guest
from app.tests.utils import create_pack_noivo_for_tests


class SignalsTestCase(TestCase):
    def setUp(self):
        # Criação de objetos Noivo e Evento
        self.user, self.custom_user, self.noivo, self.evento = create_pack_noivo_for_tests()
        self.guest = Guest.objects.create(event=self.evento, name='John Doe', is_received=False,
                                          photo_url='https://www.google.com.br/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                                          email='c@c.com', phone='999999999', confirmed=True,
                                          has_dependents=False)

    def test_create_basic_tasks_signal(self):
        tasks = Task.objects.filter(event=self.evento)
        self.assertEqual(tasks.count(), 33)

    def test_new_guest_notification_signal(self):
        notifications = Notification.objects.filter(user=self.custom_user, message__contains=self.guest.name)
        self.assertEqual(notifications.count(), 1)

    def test_rsvp_received_notification_signal(self):
        self.guest.is_received = True
        self.guest.save()
        notifications = Notification.objects.filter(user=self.custom_user, message__contains='Recebido o RSVP')
        self.assertEqual(notifications.count(), 1)
