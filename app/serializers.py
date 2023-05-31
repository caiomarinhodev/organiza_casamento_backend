from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Noivo, Event, Supplier, SupplierServicePhotos, CustomUser, Guest, Artifact, Task, Message, Idea


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class NoivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noivo
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierServicePhotosSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()

    class Meta:
        model = SupplierServicePhotos
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'email', 'confirmed', 'phone', 'photo_url', 'has_dependents', 'dependents', 'event']


class CustomUserRelatedSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CustomUser
        fields = '__all__'


class NoivoRelatedSerializer(serializers.ModelSerializer):
    custom_user = CustomUserRelatedSerializer()

    class Meta:
        model = Noivo
        fields = '__all__'


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'