from django.test import TestCase
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from app.models import Task
from app.serializers import TaskSerializer
from app.tests.utils import create_pack_noivo_for_tests


class TaskTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Criação de objetos Noivo e Evento
        self.user, self.custom_user, self.noivo, self.evento = create_pack_noivo_for_tests()

    def test_list_tasks_by_event(self):
        # Teste para listar as tarefas de um evento
        url = '/api/event/' + str(self.evento.pk) + '/tasks/'
        response = self.client.get(url)
        tasks = Task.objects.filter(event=self.evento)
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 22)

    def test_update_task(self):
        # Teste para atualizar uma tarefa
        task1 = self.evento.task_set.first()
        url = '/api/tasks/' + str(task1.pk) + '/'
        data = {'title': task1.title, 'is_completed': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(pk=task1.pk).is_completed, True)
