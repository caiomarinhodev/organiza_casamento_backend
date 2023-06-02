import datetime

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from django.utils.crypto import get_random_string
from django.utils import timezone
from random import choice, randint
from faker import Faker

from app.models import CustomUser, TypeUser, Noivo, EventSize, EventStyle, Event, Artifact, Idea, Guest


@transaction.atomic
class Command(BaseCommand):
    help = 'Cria entidades de teste para o sistema de gerenciamento de casamentos'

    def handle(self, *args, **options):
        fake = Faker()

        try:

            # Criação de usuários
            users = []
            for _ in range(2):
                username = fake.user_name()
                password = '123456'
                email = fake.email()
                user = User.objects.create_user(username=username, password=password, email=email,
                                                **{'first_name': fake.first_name(), 'last_name': fake.last_name()})
                users.append(user)
                print(f'Usuario: {username} - Senha: {password} - Email: {email}')

            custom_users = []
            for user in users:
                c_user = CustomUser.objects.create(user=user,
                                                   photo=fake.image_url(),
                                                   cep=fake.postcode(),
                                                   address=fake.street_address(),
                                                   number=randint(1, 1000),
                                                   complement=fake.text(),
                                                   district=fake.word(),
                                                   city=fake.city(),
                                                   state=fake.state_abbr(),
                                                   type=TypeUser.NOIVO)
                custom_users.append(c_user)
            print(f'custom_users: {str(len(custom_users))}')

            # Criação de noivos
            noivos = []
            for custom_user in custom_users:
                noivo = Noivo.objects.create(custom_user=custom_user,
                                             phone=fake.phone_number(),
                                             cpf='11122233399',
                                             birthdate=fake.date_of_birth()
                                             )
                noivos.append(noivo)
            print(f'noivos: {str(len(noivos))}')

            event_sizes = [choice(EventSize.choices)[0] for _ in range(2)]
            event_styles = [choice(EventStyle.choices)[0] for _ in range(2)]
            for i, noivo in enumerate(noivos):
                Event.objects.create(
                    name=fake.word(),
                    date=datetime.date.today() + datetime.timedelta(days=365),
                    groom=noivo,
                    bride=noivo,
                    size=event_sizes[i],
                    style=event_styles[i],
                    budget=fake.pydecimal(min_value=1000, max_value=10000, right_digits=2),
                    guests=150 if i == 0 else 50,
                    observation=fake.text(),
                    color1=fake.color_name(),
                    color2=fake.color_name(),
                    color3=fake.color_name(),
                    color4=fake.color_name(),
                )
            events = Event.objects.all()
            print(f'events: {str(len(events))}')

            # Criação de artefatos
            for event in events:
                for _ in range(randint(1, 6)):
                    Artifact.objects.create(
                        name=fake.word(),
                        description=fake.text(),
                        link_url=fake.url(),
                        owner=event.groom,
                        event=event,
                        public_id=fake.uuid4(),
                    )
            print(f'artifacts: {str(len(Artifact.objects.all()))}')
            # Criação de ideias
            for event in events:
                for _ in range(randint(1, 14)):
                    Idea.objects.create(
                        event=event,
                        title=fake.sentence(),
                        description=fake.text(),
                    )
            print(f'ideas: {str(len(Idea.objects.all()))}')

            # Criação de convidados
            for event in events:
                for _ in range(event.guests):
                    Guest.objects.create(
                        name=fake.name(),
                        photo_url=fake.image_url(),
                        email=fake.email(),
                        phone=fake.phone_number(),
                        confirmed=fake.boolean(),
                        has_dependents=fake.boolean(),
                        dependents=randint(0, 3),
                        event=event,
                        is_received=fake.boolean(),
                    )
            print(f'guests: {str(len(Guest.objects.all()))}')
            self.stdout.write(self.style.SUCCESS('Entidades de teste criadas com sucesso.'))
        except (Exception,):
            transaction.rollback()
            self.stdout.write(self.style.ERROR('Erro ao criar entidades de teste.'))
