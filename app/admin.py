from django.contrib import admin

from .models import Noivo, Event, Supplier, SupplierServicePhotos, CustomUser


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
    list_display = ('id', 'name', 'date', 'groom', 'bride', 'size', 'style')
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
