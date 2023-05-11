# Generated by Django 3.2.16 on 2023-05-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230509_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('photo_url', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('has_dependents', models.BooleanField(default=False)),
                ('dependents', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]