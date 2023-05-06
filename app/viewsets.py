from django.contrib.auth.models import User
from knox.auth import TokenAuthentication
from rest_framework import generics, permissions

from .models import Noivo, Event, Supplier, SupplierServicePhotos
from .serializers import NoivoSerializer, EventSerializer, SupplierSerializer, SupplierServicePhotosSerializer, \
    UserSerializer


class NoivoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Noivo.objects.all()
    serializer_class = NoivoSerializer
    permission_classes = (permissions.AllowAny,)


class NoivoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noivo.objects.all()
    serializer_class = NoivoSerializer


class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierServicePhotosListCreateAPIView(generics.ListCreateAPIView):
    queryset = SupplierServicePhotos.objects.all()
    serializer_class = SupplierServicePhotosSerializer


class SupplierServicePhotosDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierServicePhotos.objects.all()
    serializer_class = SupplierServicePhotosSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetriveAuthenticatedUser(generics.RetrieveAPIView):
    """
    Get user API endpoint.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
