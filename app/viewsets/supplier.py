from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import Supplier, SupplierServicePhotos, Message
from app.serializers import SupplierSerializer, SupplierServicePhotosSerializer, MessageSerializer


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


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    @action(detail=True, methods=['get'])
    def get_received_messages(self, request, pk=None):
        user = self.request.user
        supplier = Supplier.objects.get(custom_user__user=user)
        messages = Message.objects.filter(recipient=supplier.custom_user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
