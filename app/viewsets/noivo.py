from rest_framework import generics, permissions

from app.models import Noivo
from app.serializers import NoivoSerializer


class NoivoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Noivo.objects.all()
    serializer_class = NoivoSerializer
    permission_classes = (permissions.AllowAny,)


class NoivoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noivo.objects.all()
    serializer_class = NoivoSerializer
