# Generated by Django 3.1.7 on 2023-05-06 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230506_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noivo',
            name='custom_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='noivo', to='app.customuser'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='custom_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='app.customuser'),
        ),
    ]
