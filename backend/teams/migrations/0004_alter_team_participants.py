# Generated by Django 3.2.4 on 2021-06-27 19:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0003_alter_team_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='participants',
            field=models.ManyToManyField(related_name='Teams', to=settings.AUTH_USER_MODEL, verbose_name='Участники'),
        ),
    ]
