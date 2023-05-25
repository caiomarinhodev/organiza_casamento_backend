from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import Event, Task, PriorityChoices


@receiver(post_save, sender=Event)
def create_basic_tasks(sender, instance, created, **kwargs):
    if created:
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
        Task.objects.create(event=instance, title='Iniciar processo matrimonial na igreja', priority=PriorityChoices.MEDIUM,
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
