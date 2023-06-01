from django.contrib import admin

from .models import Noivo, Event, Supplier, SupplierServicePhotos, CustomUser, Guest, Artifact, Task, Message, Idea, \
    Notification


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    list_filter = ('type',)


@admin.register(Noivo)
class NoivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', 'phone', 'cpf', 'birthdate')
    search_fields = ('custom_user__user__first_name', 'custom_user__user__last_name', 'custom_user__user__email', 'cpf')
    list_filter = ('birthdate',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'groom', 'bride', 'size', 'style', 'budget', 'guests')
    search_fields = ('name',)
    list_filter = ('size', 'style', 'date')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', 'cnpj', 'category')
    search_fields = (
        'custom_user__user__first_name', 'custom_user__user__last_name', 'custom_user__user__email', 'cnpj')
    list_filter = ('category',)


@admin.register(SupplierServicePhotos)
class SupplierServicePhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'photo', 'price', 'description')
    search_fields = (
        'supplier__custom_user__user__first_name', 'supplier__custom_user__user__last_name',
        'supplier__custom_user__user__email')


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'name', 'email', 'confirmed', 'is_received', 'phone', 'photo_url', 'has_dependents', 'dependents', 'event')
    search_fields = ('name', 'email', 'phone', 'event__name')
    list_filter = ('confirmed', 'has_dependents', 'is_received')


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'public_id', 'link_url', 'owner', 'event', 'created_at')
    search_fields = ('name', 'description', 'event__name', 'owner__name', 'public_id')
    list_filter = ('event',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_completed', 'event', 'title', 'priority', 'recommended_date', 'due_date')
    search_fields = ('title', 'event__name')
    list_filter = ('is_completed', 'priority', 'event')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'is_read', 'date_readed',)
    search_fields = ('message', 'sender__user__username', 'recipient__user__username',
                     'sender__user__first_name', 'recipient__user__first_name',
                     'sender__user__last_name', 'recipient__user__last_name',)
    list_filter = ('is_read',)


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'event', 'created_at')
    search_fields = ('title', 'description', 'event__name',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'user', 'is_read', 'created_at')
    search_fields = ('message', 'user__user__username', 'user__user__first_name',
                     'user__user__last_name',)
    list_filter = ('is_read',)
