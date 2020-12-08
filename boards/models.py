from django.db import models
from django.contrib.auth.models import User

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


class Project(models.Model):
    """Проекты"""
    name = models.CharField("Название", max_length=150)
    prefix = models.CharField("Префикс", max_length=150)
    author = models.ForeignKey(
        User, verbose_name="Автор", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Project'
        managed = True
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


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


class Board(models.Model):
    """Доски"""
    name = models.CharField("Название", max_length=150)

    class Meta:
        db_table = 'Board'
        managed = True
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'

    def __str__(self):
        return self.name


class Tasks(models.Model):
    """Задачи"""
    executor = models.ForeignKey(
        User, verbose_name="Исполнитель", on_delete=models.SET_NULL, null=True)
    storyPoints = models.SmallIntegerField("Story Points", default=0)
    # sprint
    body = models.TextField("Body")
    board = models.ForeignKey(
        Board, verbose_name="Доска", on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'Task'
        managed = True
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
