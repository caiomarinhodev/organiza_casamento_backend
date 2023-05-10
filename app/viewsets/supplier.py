from rest_framework import generics

from app.models import Supplier, SupplierServicePhotos
from app.serializers import SupplierSerializer, SupplierServicePhotosSerializer


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
