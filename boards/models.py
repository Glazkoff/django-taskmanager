from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# class User(models.Model):
#     """Пользователи"""
#     name = models.CharField("Имя", max_length=150)
#     login = models.EmailField("Логин", max_length=254)
#     password = models.CharField("Пароль", max_length=150)
#     avatar = models.ImageField("Аватар", upload_to="users/")

#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"
#         db_table = 'User'
#         managed = True

#     def __str__(self):
#         return self.name


class Sprint(models.Model):
    """Спринты"""
    name = models.CharField("Название спринта")
    aim = models.TextField("Цель спринта")
    project = models.ForeignKey("Проект", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Sprint'
        managed = True
        verbose_name = 'Спринт'
        verbose_name_plural = 'Спринты'


class ProjectSettings(models.Model):
    """Настройки проектов"""
    teamLimit = models.SmallIntegerField("Ограничение кол-ва участников")
    sprintLimit = models.SmallIntegerField("Ограничение длительности спринта")

    class Meta:
        verbose_name = "ProjectSettings"
        verbose_name_plural = "ProjectSettingss"

    def __str__(self):
        return self.verbose_name


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
        primary_key=True
    )

    class Meta:
        db_table = 'Project'
        managed = True
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


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
    name = models.CharField("Название статуса")

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
        Project, verbose_name="Проект", on_delete=models.CASCADE)
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
        Board, verbose_name="Доска", on_delete=models.CASCADE)

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
        on_delete=models.CASCADE
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
        null=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
