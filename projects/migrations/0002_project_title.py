# Generated by Django 3.1.4 on 2021-01-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Название проекта'),
        ),
    ]
