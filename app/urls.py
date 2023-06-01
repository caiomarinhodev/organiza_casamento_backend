from django.urls import path, include
from rest_framework import routers

from app.viewsets.artifact import ArtifactViewSet
from app.viewsets.event import EventDetailAPIView, EventViewSet
from app.viewsets.guest import GuestViewSet, GuestByEventViewSet
from app.viewsets.idea import IdeaViewSet
from app.viewsets.messages import MessageViewSet
from app.viewsets.noivo import NoivoViewSet
from app.viewsets.notification import NotificationViewSet, NotificationView, MarkAllNotificationsAsReadView, \
    MarkNotificationAsReadView
from app.viewsets.reports import event_report, guest_list
from app.viewsets.supplier import SupplierViewSet
from app.viewsets.task import TaskViewSet, TaskList

urlpatterns = []

router = routers.DefaultRouter()
router.register(r'guests', GuestViewSet)
router.register(r'guests-by-event', GuestByEventViewSet)
router.register(r'noivo', NoivoViewSet, basename='noivo')
router.register(r'artifacts', ArtifactViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'ideas', IdeaViewSet)
router.register(r'events', EventViewSet)
router.register(r'notifications', NotificationViewSet)

# '/noivos/{id}/get_received_messages/'
# '/suppliers/{id}/get_received_messages/'

urlpatterns += [
    path('', include('rest_auth.urls')),
    # add admin urls
    path('registration/', include('rest_auth.registration.urls')),
    path('auth/', include('authentications.urls')),
]

urlpatterns += [
    path('event/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('event/<int:event_id>/tasks/', TaskList.as_view(), name='task-list'),
    path('event/<int:event_id>/report/csv/', event_report, name='event-report'),
    path('event/<int:event_id>/report/pdf/', guest_list, name='event-guest-report'),
    path('user/<int:user_id>/notifications/', NotificationView.as_view(), name='user-notifications'),
    path('user/<int:user_id>/notifications/mark_all_read/', MarkAllNotificationsAsReadView.as_view(),
         name='mark-all-notifications-as-read'),
    path('user/<int:user_id>/notifications/<int:notification_id>/mark_read/', MarkNotificationAsReadView.as_view(),
         name='mark-notification-as-read'),
    path('', include(router.urls)),
]
