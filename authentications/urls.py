from django.urls import path, include
from knox import views as knox_views

from authentications.viewsets import SignUpAPI, SignInAPI, RetriveAuthenticatedUser

urlpatterns = []

urlpatterns += [
    path('register/', SignUpAPI.as_view(), name='register'),
    path('login/', SignInAPI.as_view(), name='login'),
    path('user/', RetriveAuthenticatedUser.as_view(), name='user'),
    path('logout/', knox_views.LogoutView.as_view(), name="knox-logout"),
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
