from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response

from app.models import TypeUser
from app.serializers import NoivoSerializer, SupplierSerializer, CustomUserSerializer
from authentications.serializers import UserSerializer, RegisterSerializer, LoginSerializer


class SignUpAPI(generics.GenericAPIView):
    """
    Register API endpoint.
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1]
        }, status=201, headers={'Authorization': 'Token ' + token[1]})


class SignInAPI(generics.GenericAPIView):
    """
    Login API endpoint.
    """
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "type": user.profile.type,
            "profile_data": self.get_data_profile(user),
            "data_user": self.get_data_custom(user),
            "token": AuthToken.objects.create(user)[1]
        })

    def get_data_custom(self, user):
        custom_user = user.profile
        if custom_user.type == TypeUser.NOIVO:
            return NoivoSerializer(custom_user.noivo).data
        else:
            return SupplierSerializer(custom_user.supplier).data

    def get_data_profile(self, user):
        custom_user = user.profile
        return CustomUserSerializer(custom_user).data


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
