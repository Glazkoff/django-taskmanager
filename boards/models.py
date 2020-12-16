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
    name = models.CharField("Название спринта", max_length=100, unique=True)
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
        return str(self.id)


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
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
