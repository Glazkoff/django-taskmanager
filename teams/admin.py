from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html, urlencode
from django.urls import reverse
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
    list_display = ("id", "username", "first_name",
                    "last_name", "is_staff", "employee_link")
    ordering = ("employee",)

    def employee_link(self, obj):
        url = (reverse("admin:teams_employee_changelist")
               + "?"
               + urlencode({"courses__id": f"{obj.id}"}))
        return format_html('<a href="{}">{}</a>', url, obj.employee)
    employee_link.short_description = "Должность"
    employee_link.admin_order_field = 'employee'


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
