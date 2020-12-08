from django.contrib import admin
from .models import Project, Team, Board, Tasks
# Register your models here.

admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Board)
admin.site.register(Tasks)
