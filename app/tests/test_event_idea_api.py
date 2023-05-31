from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from app.models import Event, Idea


class EventIdeasAPITestCase(APITestCase):
    def setUp(self):
        self.event = Event.objects.create(name="Meu Casamento")
        self.idea1 = Idea.objects.create(event=self.event, title="Ideia 1", description="Descrição da Ideia 1")
        self.idea2 = Idea.objects.create(event=self.event, title="Ideia 2", description="Descrição da Ideia 2")

    def test_list_event_ideas(self):
        url = reverse('event-ideas', args=[self.event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
