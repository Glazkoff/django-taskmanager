from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from projects.models import Project, Sprint


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teamRole = models.CharField("Роль в команде", max_length=100)

    def __str__(self):
        return self.teamRole

    class Meta:
        managed = True
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Board(models.Model):
    """Доски"""
    name = models.CharField("Название", max_length=150)
    team = models.ForeignKey(
        "Team",
        verbose_name="Команда",
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'Board'
        managed = True
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'

    def __str__(self):
        return self.name


class Status(models.Model):
    board = models.ForeignKey(
        Board,
        verbose_name="Доска",
        on_delete=models.CASCADE
    )
    name = models.CharField("Название статуса", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Status'
        managed = True
        verbose_name = 'Статус задач'
        verbose_name_plural = 'Статусы задач'


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


class Task(models.Model):
    """Задачи"""
    executor = models.ForeignKey(
        User, verbose_name="Исполнитель", on_delete=models.SET_NULL, null=True)
    storyPoints = models.SmallIntegerField("Story Points", default=0)
    body = models.TextField("Тело задачи")
    board = models.ForeignKey(
        Board, verbose_name="Доска",
        on_delete=models.CASCADE
    )
    sprint = models.ForeignKey(
        Sprint,
        verbose_name="Спринт",
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    status = models.ForeignKey(
        Status, verbose_name="Статус",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        # TODO: добавить ограничение внешнего ключа
        # https://overcoder.net/q/142430/django-foreignkey-limitchoicesto-%D1%80%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82%D1%83-%D1%82%D0%B5%D0%BA%D1%83%D1%89%D0%B5%D0%B3%D0%BE-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%B0
        # limit_choices_to={'board': "self.board.id"}
    )

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'Task'
        managed = True
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comment(models.Model):

    task = models.ForeignKey(
        Task,
        verbose_name="Задача",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Автор",
        on_delete=models.CASCADE
    )
    body = models.TextField("Тело комментария")
    parent = models.ForeignKey(
        "self",
        verbose_name="Родительский комментарий",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="children")

    def __str__(self):
        return self.body

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
