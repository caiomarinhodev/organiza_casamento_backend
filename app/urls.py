from django.urls import path, include
from rest_framework import routers

from app.viewsets.event import EventDetailAPIView
from app.viewsets.guest import GuestViewSet, GuestByEventViewSet
from app.viewsets.noivo import NoivoViewSet

urlpatterns = []

router = routers.DefaultRouter()
router.register(r'guests', GuestViewSet)
router.register(r'guests-by-event', GuestByEventViewSet)
router.register(r'noivo', NoivoViewSet, basename='noivo')

urlpatterns += [
    path('', include('rest_auth.urls')),
    # add admin urls
    path('registration/', include('rest_auth.registration.urls')),
    path('auth/', include('authentications.urls')),
]

urlpatterns += [
    path('event/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('', include(router.urls)),
]
