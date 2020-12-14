from django.contrib import admin
from .models import Sprint, ProjectSettings, Project, Board, Status, Team, Task, Comment
# Register your models here.

admin.site.register(Sprint)
admin.site.register(ProjectSettings)
admin.site.register(Project)
admin.site.register(Board)
admin.site.register(Status)
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(Comment)
