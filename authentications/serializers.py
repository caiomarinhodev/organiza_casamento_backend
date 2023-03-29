from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """

    class Meta:
        ref_name = "User"
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    """
    Register serializer
    """

    class Meta:
        ref_name = "Register User"
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        This method is used to create a new user
        """
        if 'email' not in validated_data:
            raise serializers.ValidationError({'email': 'This field is required'})
        if 'username' not in validated_data:
            raise serializers.ValidationError({'username': 'This field is required'})
        if 'password' not in validated_data:
            raise serializers.ValidationError({'password': 'This field is required'})
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    class Meta:
        ref_name = "Login User"

    """
    Login serializer
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        """
        This method is called when .is_valid() is called on the serializer class
        """
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
