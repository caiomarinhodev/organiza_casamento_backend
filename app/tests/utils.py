from django.contrib.auth.models import User

from app.models import CustomUser, TypeUser, Noivo, Event, EventSize, EventStyle


def create_pack_noivo_for_tests():
    user = User.objects.create_user(
        username='joao', password='123456',
        first_name='João', last_name='Silva',
        email='joao@google.com'
    )
    custom_user = CustomUser.objects.create(
        user=user,
        type=TypeUser.NOIVO,
        photo='',
        cep='58434000',
        address='Rua João Pessoa',
        number='123',
        complement='',
        district='Centro',
        city='Campina Grande',
        state='PB',
    )

    noivo = Noivo.objects.create(
        custom_user=custom_user,
        phone='83999999999',
        cpf='11111111111',
        birthdate='1990-01-01',
    )
    evento = Event.objects.create(
        groom=noivo,
        name='Casamento do João',
        date='2024-05-30',
        size=EventSize.MEDIUM_WEDDING,
        style=EventStyle.MODERN_MINIMALIST
    )

    return user, custom_user, noivo, evento
