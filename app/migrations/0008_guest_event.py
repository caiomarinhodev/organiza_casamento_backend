# Generated by Django 3.2.16 on 2023-05-10 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.event'),
        ),
    ]
