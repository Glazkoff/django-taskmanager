from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teamRole = models.CharField("Роль в команде", max_length=100)

    def __str__(self):
        return self.teamRole

    class Meta:
        managed = True
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Team(models.Model):
    """Команды"""
    name = models.CharField("Название", max_length=150)
    leader = models.ForeignKey(
        User, verbose_name="Лидер", on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(
        Project, verbose_name="Проект", on_delete=models.CASCADE, related_name="teams")
    participants = models.ManyToManyField(
        User, verbose_name="Участники", related_name="Teams")

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def __str__(self):
        return self.name
