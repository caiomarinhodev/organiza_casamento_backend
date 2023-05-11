from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from app.models import Noivo
from app.serializers import NoivoSerializer, NoivoRelatedSerializer


class NoivoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Noivo.objects.all()
    serializer_class = NoivoSerializer
    permission_classes = (permissions.AllowAny,)


class NoivoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noivo.objects.all()
    serializer_class = NoivoSerializer


class NoivoViewSet(viewsets.ModelViewSet):
    serializer_class = NoivoRelatedSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Noivo.objects.filter(custom_user__user=user)
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        custom_user = instance.custom_user
        profile = instance.custom_user.user
        new_custom_user = self.request.data['custom_user']
        new_user = self.request.data['custom_user']['user']
        profile.first_name = new_user['first_name']
        profile.last_name = new_user['last_name']
        profile.email = new_user['email']
        profile.save()
        custom_user.cep = new_custom_user['cep']
        custom_user.address = new_custom_user['address']
        custom_user.number = new_custom_user['number']
        custom_user.complement = new_custom_user['complement']
        custom_user.district = new_custom_user['district']
        custom_user.city = new_custom_user['city']
        custom_user.state = new_custom_user['state']
        custom_user.save()
        request.data.pop('custom_user')
        instance = self.get_object()
        serializer = NoivoSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
