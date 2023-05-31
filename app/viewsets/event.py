from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import Event
from app.serializers import EventSerializer, IdeaSerializer


class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=True, methods=['GET'])
    def ideas(self, request, pk=None):
        event = self.get_object()
        ideas = event.idea_set.all()
        serializer = IdeaSerializer(ideas, many=True)
        return Response(serializer.data)
