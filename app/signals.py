from datetime import timedelta, datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from app.models import Event, Task, PriorityChoices, Notification, CustomUser, Guest


@receiver(post_save, sender=Event)
def create_basic_tasks(sender, instance, created, **kwargs):
    if created:
        # Cria uma notificação informando sobre as tarefas iniciais
        notification = Notification.objects.create(
            user=instance.groom.custom_user,
            message='Lembre-se de preencher os dados do Evento e do Perfil.'
        )
        notification.save()
        Task.objects.create(event=instance, title='Definir data do casamento', priority=PriorityChoices.HIGH,
                            recommended_date='12 meses antes')
        Task.objects.create(event=instance, title='Escolher local da cerimônia', priority=PriorityChoices.HIGH,
                            recommended_date='12 meses antes')
        Task.objects.create(event=instance, title='Escolher local da festa', priority=PriorityChoices.HIGH,
                            recommended_date='12 meses antes')
        Task.objects.create(event=instance, title='Elaborar lista de convidados', priority=PriorityChoices.HIGH,
                            recommended_date='12 meses antes')
        Task.objects.create(event=instance, title='Contratar cerimonialista', priority=PriorityChoices.HIGH,
                            recommended_date='12 meses antes')
        Task.objects.create(event=instance, title='Preparar convites', priority=PriorityChoices.HIGH,
                            recommended_date='12 meses antes')
        Task.objects.create(event=instance, title=' Pesquisar destinos da lua de mel', priority=PriorityChoices.MEDIUM,
                            recommended_date='8 meses antes')
        Task.objects.create(event=instance, title='Contratar alianças', priority=PriorityChoices.MEDIUM,
                            recommended_date='8 meses antes')
        Task.objects.create(event=instance, title='Envie o save the date', priority=PriorityChoices.MEDIUM,
                            recommended_date='6 meses antes')
        Task.objects.create(event=instance, title='Contratar decoração', priority=PriorityChoices.MEDIUM,
                            recommended_date='6 meses antes')
        Task.objects.create(event=instance, title='Contratar fornecedores de música', priority=PriorityChoices.MEDIUM,
                            recommended_date='6 meses antes')
        Task.objects.create(event=instance, title='Escolher bolo e doces', priority=PriorityChoices.MEDIUM,
                            recommended_date='6 meses antes')
        Task.objects.create(event=instance, title='Escolher vestido da noiva', priority=PriorityChoices.MEDIUM,
                            recommended_date='6 meses antes')
        Task.objects.create(event=instance, title='Escolher traje do noivo', priority=PriorityChoices.MEDIUM,
                            recommended_date='6 meses antes')
        Task.objects.create(event=instance, title='Iniciar processo matrimonial na igreja',
                            priority=PriorityChoices.MEDIUM,
                            recommended_date='4 meses antes')
        Task.objects.create(event=instance, title='Contratar buffet', priority=PriorityChoices.MEDIUM,
                            recommended_date='4 meses antes')
        Task.objects.create(event=instance, title='Enviar convites', priority=PriorityChoices.MEDIUM,
                            recommended_date='3 meses antes')
        Task.objects.create(event=instance, title='Contratar fotógrafo', priority=PriorityChoices.MEDIUM,
                            recommended_date='3 meses antes')
        Task.objects.create(event=instance, title='Escolher lembrancinhas', priority=PriorityChoices.LOW,
                            recommended_date='3 meses antes')
        Task.objects.create(event=instance, title='Escolher alianças', priority=PriorityChoices.LOW,
                            recommended_date='3 meses antes')
        Task.objects.create(event=instance, title='Escolher padrinhos', priority=PriorityChoices.LOW,
                            recommended_date='3 meses antes')
        Task.objects.create(event=instance, title='Escolher madrinhas', priority=PriorityChoices.LOW,
                            recommended_date='3 meses antes')
        Task.objects.create(event=instance, title='Escolher daminhas e pajens', priority=PriorityChoices.LOW,
                            recommended_date='3 meses antes')
        Task.objects.create(event=instance, title='Escolher buquê', priority=PriorityChoices.LOW,
                            recommended_date='2 meses antes')
        Task.objects.create(event=instance, title='Entregar documentação na igreja', priority=PriorityChoices.LOW,
                            recommended_date='2 meses antes')
        Task.objects.create(event=instance, title='Entrada documentação do cartório', priority=PriorityChoices.LOW,
                            recommended_date='2 meses antes')
        Task.objects.create(event=instance, title='Degustação do cardápio', priority=PriorityChoices.LOW,
                            recommended_date='2 meses antes')
        Task.objects.create(event=instance, title='Organizar chá de cozinha', priority=PriorityChoices.LOW,
                            recommended_date='2 meses antes')
        Task.objects.create(event=instance, title='Teste de cabelo e maquiagem', priority=PriorityChoices.LOW,
                            recommended_date='1 mês antes')
        Task.objects.create(event=instance, title='Realizar ensaio fotográfico', priority=PriorityChoices.LOW,
                            recommended_date='1 mês antes')
        Task.objects.create(event=instance, title='Reuniao final no espaço', priority=PriorityChoices.LOW,
                            recommended_date='Semana do evento')
        Task.objects.create(event=instance, title='Retirar vestido e trajes', priority=PriorityChoices.LOW,
                            recommended_date='Semana do evento')
        Task.objects.create(event=instance, title='Verificar pagamentos', priority=PriorityChoices.LOW,
                            recommended_date='Semana do evento')


@receiver(post_save, sender=Guest)
def new_guest_notification(sender, instance, created, **kwargs):
    if created:
        notification = Notification.objects.create(
            user=instance.event.groom.custom_user,
            message=f'Novo convidado "{instance.name}" adicionado. Envie o RSVP.'
        )
        notification.save()


@receiver(post_save, sender=Guest)
def rsvp_received_notification(sender, instance, **kwargs):
    # Verifica se o RSVP foi recebido
    if instance.is_received:
        # Cria uma notificação de RSVP recebido
        notification = Notification.objects.create(
            user=instance.event.groom.custom_user,
            message=f'Recebido o RSVP de "{instance.name}".'
        )
        notification.save()


def convert_to_date(str_date: str):
    return datetime.strptime(str_date, '%Y-%m-%d').date()


@receiver(post_save, sender=Event)
def send_upcoming_event_notification(sender, instance, **kwargs):
    if instance.date:
        if instance.date - timezone.now().date() <= timezone.timedelta(days=30):
            notification = Notification.objects.create(
                user=instance.groom.custom_user,
                message=f'Data importante se aproximando. '
                        f'Verifique se todas as tarefas estão concluídas.'
            )
            notification.save()
