from django.contrib import admin
from .models import Sprint, ProjectSettings, Project, Board, Status, Team, Task, Comment
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class TeamInline(admin.TabularInline):
    model = Team
    extra = 0
    readonly_fields = ("id", "name")
    classes = ("collapse",)


class SettingsInline(admin.TabularInline):
    model = ProjectSettings
    extra = 0

# Project


class ProjectResource(resources.ModelResource):
    """Ресурс проекта для импорта"""
    class Meta:
        model = Project


class ProjectAdmin(ImportExportModelAdmin):
    actions = ['publish', 'unpublish']
    list_display = ("id", "name", "prefix", "leader", "settings", "draft")
    list_display_links = ("id", "name",)
    list_filter = ("leader", )
    search_fields = ["name", "leader__username", ]
    readonly_fields = ("id",)
    inlines = [TeamInline, SettingsInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    fieldsets = (
        ("Главное", {
            "fields": (
                ("name", "prefix"), "leader"
            ),
        }),
    )
    resource_class = ProjectResource

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись обновлена"
        else:
            message_bit = f"{row_update} записей было обновлено"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись обновлена"
        else:
            message_bit = f"{row_update} записей было обновлено"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ("change",)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ("change",)


admin.site.register(Project, ProjectAdmin)


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


# Sprint

class SprintResource(resources.ModelResource):
    """Ресурс спринт для импорта"""
    class Meta:
        model = Sprint


class SprintAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "aim", "project", "startDate", "finishDate")
    list_display_links = ("id", "name")
    list_filter = ("project",)
    search_fields = ["name", "project__name"]
    readonly_fields = ("aim", "project")
    resource_class = SprintResource


# ProjectSettings

class ProjectSettingsResource(resources.ModelResource):
    """Ресурс настроек проекта для импорта"""
    class Meta:
        model = ProjectSettings


class ProjectSettingsAdmin(ImportExportModelAdmin):
    list_display = ("id", "project", "teamLimit", "sprintLimit")
    list_display_links = ("id",)
    list_filter = ("project",)
    search_fields = ["project__name"]
    readonly_fields = ("project",)
    resource_class = ProjectSettingsResource


admin.site.register(ProjectSettings, ProjectSettingsAdmin)

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
