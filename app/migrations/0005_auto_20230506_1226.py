# Generated by Django 3.1.7 on 2023-05-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20230506_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
    ]
