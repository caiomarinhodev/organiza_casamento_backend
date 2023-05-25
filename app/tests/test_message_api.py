from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Noivo, Supplier, Message, CustomUser, TypeUser, SupplierType
from app.tests.utils import create_pack_noivo_for_tests


class MessageAPITestCase(APITestCase):
    def setUp(self):
        self.user, self.custom_user, self.noivo, self.evento = create_pack_noivo_for_tests()

        user_supplier = User.objects.create_user(username='supplier1',
                                                 password='supplier1',
                                                 first_name='Supplier',
                                                 last_name='1', )
        custom_user_supplier = CustomUser.objects.create(user=user_supplier,
                                                         type=TypeUser.SUPPLIER)
        self.supplier = Supplier.objects.create(custom_user=custom_user_supplier,
                                                category=SupplierType.DECORATION)

        self.message = Message.objects.create(sender=self.supplier.custom_user,
                                              recipient=self.noivo.custom_user,
                                              content='Test message')

    def test_create_message(self):
        url = reverse('message-list')
        data = {
            'sender': self.supplier.custom_user.id,
            'recipient': self.noivo.custom_user.id,
            'content': 'New message'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 2)

    def test_retrieve_message(self):
        url = reverse('message-detail', args=[self.message.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], self.message.content)

    def test_update_message(self):
        url = reverse('message-detail', args=[self.message.id])
        data = {
            'sender': self.message.sender.id,
            'recipient': self.message.recipient.id,
            'content': 'Updated message'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], 'Updated message')
        self.message.refresh_from_db()
        self.assertEqual(self.message.content, 'Updated message')

    def test_delete_message(self):
        url = reverse('message-detail', args=[self.message.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Message.objects.filter(id=self.message.id).exists())

    # def test_get_received_messages(self):
    #     url = reverse('noivo-get-received-messages', args=[self.noivo.id])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data[0]['content'], self.message.content)
