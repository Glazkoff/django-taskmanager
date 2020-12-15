from django.contrib import admin
from .models import Sprint, ProjectSettings, Project, Board, Status, Team, Task, Comment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "prefix", "leader", "settings")
    list_display_links = ("id", "name",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "project", "leader")
    list_display_links = ("id", "name")
    list_filter = ("leader", "project",)


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "team")
    list_display_links = ("id", "name")


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "aim", "project", "startDate", "finishDate")
    list_display_links = ("id", "name")


@admin.register(ProjectSettings)
class ProjectSettingsAdmin(admin.ModelAdmin):
    list_display = ("id", "teamLimit", "sprintLimit")
    list_display_links = ("id",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "board", "name")
    list_display_links = ("id", "name")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "body", "executor", "status", "sprint", "board")
    list_display_links = ("id", "body")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "body", "author", "task", "parent")
    list_display_links = ("id", "body")
