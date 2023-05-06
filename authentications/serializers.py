from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Noivo, Supplier, TypeUser, CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """

    class Meta:
        ref_name = "User"
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=TypeUser.choices)

    class Meta:
        ref_name = "Register User"
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        This method is used to create a new user
        """
        if 'type' not in validated_data:
            raise serializers.ValidationError({'type': 'This field is required'})
        if 'email' not in validated_data:
            raise serializers.ValidationError({'email': 'This field is required'})
        if 'username' not in validated_data:
            raise serializers.ValidationError({'username': 'This field is required'})
        if 'password' not in validated_data:
            raise serializers.ValidationError({'password': 'This field is required'})

        # create user with validated data if type is noivo
        if validated_data['type'] == TypeUser.NOIVO:
            try:
                user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                                validated_data['password'],
                                                **{'first_name': validated_data['first_name'],
                                                   'last_name': validated_data['last_name']}
                                                )
                custom_user = CustomUser.objects.create(user=user, type=TypeUser.NOIVO)
                Noivo.objects.create(custom_user=custom_user)
                return user
            except Exception as e:
                raise serializers.ValidationError({'detail': str(e)})
        else:
            try:
                user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                                validated_data['password'],
                                                **{'first_name': validated_data['first_name'],
                                                   'last_name': validated_data['last_name']}
                                                )
                custom_user = CustomUser.objects.create(user=user, type=TypeUser.SUPPLIER)
                Supplier.objects.create(custom_user=custom_user)
                return user
            except Exception as e:
                raise serializers.ValidationError({'detail': str(e)})


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
