# Generated by Django 3.2.16 on 2023-05-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='recommended_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
