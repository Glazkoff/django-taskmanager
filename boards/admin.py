from django.contrib import admin
from .models import Sprint, ProjectSettings, Project, Board, Status, Team, Task, Comment


class TeamInline(admin.TabularInline):
    model = Team
    extra = 0
    readonly_fields = ("id", "name")
    classes = ("collapse",)


class SettingsInline(admin.TabularInline):
    model = ProjectSettings
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
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


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "project", "leader")
    list_display_links = ("id", "name")
    list_filter = ("leader", "project")
    search_fields = ["name", "project__name", "leader__username", ]
    readonly_fields = ("id",)


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "team")
    list_display_links = ("id", "name")
    list_filter = ("team",)
    search_fields = ["name", "team__name"]
    readonly_fields = ("id",)


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "aim", "project", "startDate", "finishDate")
    list_display_links = ("id", "name")
    list_filter = ("project",)
    search_fields = ["name", "project__name"]
    readonly_fields = ("aim", "project")


@admin.register(ProjectSettings)
class ProjectSettingsAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "teamLimit", "sprintLimit")
    list_display_links = ("id",)
    list_filter = ("project",)
    search_fields = ["project__name"]
    readonly_fields = ("project",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "board", "name")
    list_display_links = ("id", "name")
    list_filter = ("board",)
    search_fields = ["name", "board__name"]
    readonly_fields = ("id", "board")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "body", "executor", "status", "sprint", "board")
    list_display_links = ("id", "body")
    list_filter = ("board", "executor",)
    search_fields = ["executor_username", "board__name"]
    readonly_fields = ("id", "board")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "body", "author", "task", "parent")
    list_display_links = ("id", "body")
    list_filter = ("author",)
    search_fields = ["body", "author__username"]
    readonly_fields = ("id", "author", "task", "parent")
