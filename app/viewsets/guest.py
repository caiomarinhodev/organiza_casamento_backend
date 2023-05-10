from rest_framework import viewsets
from rest_framework.response import Response

from app.models import Guest
from app.serializers import GuestSerializer


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GuestByEventViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def list(self, request, *args, **kwargs):
        event_id = request.query_params.get('event', None)
        queryset = self.get_queryset()

        if event_id is not None:
            queryset = queryset.filter(event_id=event_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
