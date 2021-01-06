from django.contrib import admin
from .models import ProjectSettings, Project, Sprint
from boards.models import Team
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Project


class ProjectResource(resources.ModelResource):
    """Ресурс проекта для импорта"""
    class Meta:
        model = Project


class TeamInline(admin.TabularInline):
    model = Team
    extra = 0
    readonly_fields = ("id", "name")
    classes = ("collapse",)


class SettingsInline(admin.TabularInline):
    model = ProjectSettings
    extra = 0


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
    resource_class = SprintResource


admin.site.register(Sprint, SprintAdmin)


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
