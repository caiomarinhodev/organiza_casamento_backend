from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from app.models import Event, Idea
from app.tests.utils import create_pack_noivo_for_tests


class IdeaAPITestCase(APITestCase):
    def setUp(self):
        self.user, self.custom_user, self.noivo, self.event = create_pack_noivo_for_tests()
        self.idea = Idea.objects.create(event=self.event, title="Ideia 1", description="Descrição da Ideia 1")

    def test_list_ideas(self):
        url = reverse('idea-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.idea.title)

    def test_create_idea(self):
        url = reverse('idea-list')
        data = {'event': self.event.id, 'title': 'Nova Ideia', 'description': 'Descrição da Nova Ideia'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Idea.objects.count(), 2)

    def test_retrieve_idea(self):
        url = reverse('idea-detail', args=[self.idea.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.idea.title)

    def test_update_idea(self):
        url = reverse('idea-detail', args=[self.idea.id])
        data = {'title': 'Ideia Atualizada'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.idea.refresh_from_db()
        self.assertEqual(self.idea.title, 'Ideia Atualizada')

    def test_delete_idea(self):
        url = reverse('idea-detail', args=[self.idea.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Idea.objects.count(), 0)
