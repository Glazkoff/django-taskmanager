from django.contrib import admin
from .models import Board, Status, Team, Task, Comment, Employee
from projects.models import ProjectSettings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin

admin.site.site_title = "Таск-менеджер"
admin.site.site_header = "Админпанель таск-менеджера"
admin.site.index_title = "Админпанель"

# Переорпределение User


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'Роль'
    verbose_name_plural = 'Роли'


class MyUserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)


# Team

class TeamResource(resources.ModelResource):
    """Ресурс команды для импорта"""
    class Meta:
        model = Team


class TeamAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "project", "leader")
    list_display_links = ("id", "name")
    list_filter = ("leader", "project")
    search_fields = ["name", "project__name", "leader__username", ]
    readonly_fields = ("id",)
    resource_class = TeamResource


admin.site.register(Team, TeamAdmin)


# Board

class BoardResource(resources.ModelResource):
    """Ресурс доски для импорта"""
    class Meta:
        model = Board


class BoardAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "team")
    list_display_links = ("id", "name")
    list_filter = ("team",)
    search_fields = ["name", "team__name"]
    readonly_fields = ("id",)
    resource_class = BoardResource


admin.site.register(Board, BoardAdmin)


# Status


class StatusResource(resources.ModelResource):
    """Ресурс статусов проекта для импорта"""
    class Meta:
        model = Status


class StatusAdmin(ImportExportModelAdmin):
    list_display = ("id", "board", "name")
    list_display_links = ("id", "name")
    list_filter = ("board",)
    search_fields = ["name", "board__name"]
    readonly_fields = ("id", "board")
    resource_class = StatusResource


admin.site.register(Status, StatusAdmin)

# Task


class TaskResource(resources.ModelResource):
    """Ресурс задач для импорта"""
    class Meta:
        model = Task


class TaskAdmin(ImportExportModelAdmin):
    list_display = ("id", "body", "executor", "status", "sprint", "board")
    list_display_links = ("id", "body")
    list_filter = ("board", "executor",)
    search_fields = ["executor_username", "board__name"]
    readonly_fields = ("id", "board")
    resource_class = TaskResource


admin.site.register(Task, TaskAdmin)

# Comment


class CommentResource(resources.ModelResource):
    """Ресурс комментария проекта для импорта"""
    class Meta:
        model = Comment


class CommentAdmin(ImportExportModelAdmin):
    list_display = ("id", "body", "author", "task", "parent")
    list_display_links = ("id", "body")
    list_filter = ("author",)
    search_fields = ["body", "author__username"]
    readonly_fields = ("id", "author", "task", "parent")
    resource_class = CommentResource


admin.site.register(Comment, CommentAdmin)
