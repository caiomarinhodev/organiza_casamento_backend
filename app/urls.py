from django.contrib import admin
from django.urls import path, include

urlpatterns = []

urlpatterns += [
    path('', include('rest_auth.urls')),
    # add admin urls
    path('registration/', include('rest_auth.registration.urls')),
    path('auth/', include('authentications.urls')),
]
