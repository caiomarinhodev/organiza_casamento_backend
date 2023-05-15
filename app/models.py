from django.contrib.auth.models import User
from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(Timestamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.TextField(blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    complement = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class TypeUser(models.TextChoices):
    NOIVO = 'NOIVO'
    SUPPLIER = 'FORNECEDOR'


class CustomUser(Profile):
    type = models.CharField(max_length=20, blank=True, null=True, choices=TypeUser.choices, default=TypeUser.NOIVO)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.user.first_name


class Noivo(Timestamp):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='noivo')
    phone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Noivo'
        verbose_name_plural = 'Noivos'

    def __str__(self):
        return self.custom_user.user.first_name


class EventSize(models.TextChoices):
    ELOPMENT_WEDDING = 'Elopment Wedding'
    MINI_WEDDING = 'Mini Wedding'
    SMALL_WEDDING = 'Casamento Pequeno'
    MEDIUM_WEDDING = 'Casamento Médio'
    BIG_WEDDING = 'Casamento Grande'
    MEGA_WEDDING = 'Mega Wedding'
    DESTINATION_WEDDING = 'Destination Wedding'


class EventStyle(models.TextChoices):
    CLASSIC_TRADITIONAL = 'Classico / Tradicional'
    MODERN_MINIMALIST = 'Moderno / Minimalista'
    VINTAGE_RUSTIC = 'Vintage / Rustico'
    BEACH_COUNTRYSIDE = 'Praia / Campo'
    THEMATIC = 'Temático'


class Event(Timestamp):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    groom = models.ForeignKey(Noivo, on_delete=models.CASCADE, related_name='groom', blank=True, null=True,
                              related_query_name='groom')
    bride = models.ForeignKey(Noivo, on_delete=models.CASCADE, related_name='bride', blank=True, null=True)
    size = models.CharField(max_length=100, choices=EventSize.choices, default=EventSize.MEDIUM_WEDDING)
    style = models.CharField(max_length=100, choices=EventStyle.choices, default=EventStyle.CLASSIC_TRADITIONAL)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    guests = models.IntegerField(blank=True, null=True, default=100)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.name


class SupplierType(models.TextChoices):
    CERYMONY_RECEPTION = 'Cerimônia e Recepção'
    BUFFET_CATERING = 'Buffet e Catering'
    DECORATION = 'Decoração'
    PHOTOGRAPHY_VIDEO = 'Fotografia e Vídeo'
    MUSIC_ENTERTEINMENT = 'Música e Entretenimento'
    WEDDING_DRESS_ATTIRE = 'Vestido e Traje'
    INVITATIONS_PAPER_GOODS = 'Convites e Papelaria'
    HAIR_MAKEUP = 'Cabelo e Maquiagem'
    TRANSPORTATION = 'Transporte'
    SOUVENIRS_GIFTS = 'Lembrancinhas e Presentes'
    OTHERS = 'Outros'


class Supplier(Timestamp):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='supplier')
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=100, choices=SupplierType.choices, default=SupplierType.OTHERS)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.custom_user.user.first_name


class SupplierServicePhotos(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    photo = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Foto do Fornecedor'
        verbose_name_plural = 'Fotos dos Fornecedores'

    def __str__(self):
        return self.supplier.custom_user.user.first_name


class Guest(Timestamp):
    name = models.CharField(max_length=255)
    photo_url = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    has_dependents = models.BooleanField(default=False)
    dependents = models.IntegerField(blank=True, null=True, default=0)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Artifact(Timestamp):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link_url = models.URLField(blank=True, null=True)
    owner = models.ForeignKey(Noivo, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    public_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class PriorityChoices(models.TextChoices):
    LOW = 'Baixo'
    MEDIUM = 'Médio'
    HIGH = 'Alto'


class Task(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    priority = models.CharField(choices=PriorityChoices.choices, default=PriorityChoices.MEDIUM, max_length=100)
    recommended_date = models.CharField(max_length=255, blank=True, null=True)
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def complete_task(self):
        self.is_completed = True
        self.save(update_fields=['is_completed'])
