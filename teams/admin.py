from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Team, Employee
from import_export.admin import ImportExportModelAdmin
from import_export import resources

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


class EmployeeResource(resources.ModelResource):
    """Ресурс сотрудника для импорта"""
    class Meta:
        model = Employee


class EmployeeAdmin(ImportExportModelAdmin):
    readonly_fields = ("id",)
    resource_class = EmployeeResource


admin.site.register(Employee, EmployeeAdmin)


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
