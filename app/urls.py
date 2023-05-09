from django.contrib import admin
from django.urls import path, include

from app.viewsets import EventDetailAPIView

urlpatterns = []

urlpatterns += [
    path('', include('rest_auth.urls')),
    # add admin urls
    path('registration/', include('rest_auth.registration.urls')),
    path('auth/', include('authentications.urls')),
]

urlpatterns += [
    path('event/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
]
