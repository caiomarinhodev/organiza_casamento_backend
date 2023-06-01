from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Notification, Task, CustomUser
from app.serializers import NotificationSerializer


def get_months_from_text(text):
    content = text.split(' ')[0]
    if content == 'Semana':
        return 0
    return int(content)


def get_date_from_months(months: int, event_date: timezone.datetime):
    try:
        if months == 0:
            return event_date - timezone.timedelta(days=7)
        return event_date - timezone.timedelta(days=months * 30)
    except (Exception,):
        return None


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationView(APIView):

    def check_exists_notifications(self, custom_user, message):
        return Notification.objects.filter(user=custom_user, message=message).exists()

    def check_notifications(self, user):
        custom_user = CustomUser.objects.get(user=user)
        tasks = Task.objects.all()
        for task in tasks:
            months = get_months_from_text(task.recommended_date)
            today = timezone.now().date()
            event_date = task.event.date if task.event.date else None
            recommended_date = get_date_from_months(months, event_date)
            if recommended_date and recommended_date <= today:
                if self.check_exists_notifications(
                        custom_user=custom_user,
                        message=f'A tarefa "{task.title}" está passada da data recomendada.'):
                    continue
                # Cria um alerta de tarefa pendente para a data recomendada
                notification = Notification.objects.create(
                    user=custom_user,
                    message=f'A tarefa "{task.title}" está passada da data recomendada.'
                )
                notification.save()
            elif recommended_date and (
                    recommended_date <= today and recommended_date == event_date - timedelta(days=7)):
                if self.check_exists_notifications(
                        custom_user=custom_user,
                        message=f'A tarefa "{task.title}" está próxima da data recomendada.'):
                    continue
                # Cria um alerta de tarefa pendente para a data recomendada
                notification = Notification.objects.create(
                    user=CustomUser.objects.get(user=user),
                    message=f'A tarefa "{task.title}" está próxima da data recomendada.'
                )
                notification.save()

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        user = User.objects.get(pk=user_id)
        self.check_notifications(user)
        custom_user = CustomUser.objects.get(user=user)
        notifications = Notification.objects.filter(user=custom_user)
        serialized_notifications = NotificationSerializer(notifications, many=True)
        return Response(serialized_notifications.data)


class MarkAllNotificationsAsReadView(APIView):
    def post(self, request, user_id, format=None):
        try:
            user = User.objects.get(pk=user_id)
            custom_user = CustomUser.objects.get(user=user)
            notifications = Notification.objects.filter(user__pk=custom_user.pk, is_read=False)
            for notification in notifications:
                notification.read_notification()
            return Response(status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MarkNotificationAsReadView(APIView):
    def post(self, request, user_id, notification_id, format=None):
        try:
            notification = Notification.objects.get(pk=notification_id, is_read=False)
            notification.is_read = True
            notification.save()
            return Response(status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
