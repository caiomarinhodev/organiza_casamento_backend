import json

from rest_framework import viewsets, generics
from rest_framework.response import Response

from app.models import Task
from app.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        filter = request.query_params.get('filter')
        filters = json.loads(filter)['filters']
        event_id = filters.get('event_id')
        queryset = self.get_queryset()

        if event_id is not None:
            queryset = queryset.filter(event_id=event_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TaskList(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Task.objects.filter(event_id=event_id)
