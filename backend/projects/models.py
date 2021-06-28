from django.db import models
from django.conf import settings


class ProjectSettings(models.Model):
    """Настройки проектов"""
    teamLimit = models.SmallIntegerField("Ограничение кол-ва участников")
    sprintLimit = models.SmallIntegerField("Ограничение длительности спринта")
    project = models.OneToOneField(
        "Project",
        verbose_name="Проекты",
        on_delete=models.CASCADE,
        related_name="project"
    )

    class Meta:
        verbose_name = "Настроки проекта"
        verbose_name_plural = "Настройки проектов"

    def __str__(self):
        return str(f'Ограничения: участники - {self.teamLimit}, длительность - {self.sprintLimit} ')


class Project(models.Model):
    """Проекты"""
    name = models.CharField("Название проекта", max_length=150)
    prefix = models.CharField("Префикс", max_length=150)
    leader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Лидер проекта",
        on_delete=models.CASCADE)
    settings = models.OneToOneField(
        ProjectSettings,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name="settings",
        verbose_name="Настройки",
        default=None,
        null=True,
        blank=True
    )
    draft = models.BooleanField("Черновик", default=False)

    class Meta:
        db_table = 'Project'
        managed = True
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class Sprint(models.Model):
    """Спринты"""
    name = models.CharField("Название спринта", max_length=100)
    aim = models.TextField("Цель спринта")
    project = models.ForeignKey(
        "Project",
        verbose_name="Проект",
        on_delete=models.CASCADE)
    startDate = models.DateField(
        verbose_name="Начало спринта", null=True, blank=True)
    finishDate = models.DateField(
        verbose_name="Окончание спринта", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Sprint'
        managed = True
        verbose_name = 'Спринт'
        verbose_name_plural = 'Спринты'
