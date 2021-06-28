# Generated by Django 3.2.4 on 2021-06-27 19:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0002_auto_20210616_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='Teams', to=settings.AUTH_USER_MODEL, verbose_name='Участники'),
        ),
    ]
