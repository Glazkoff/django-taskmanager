
from django.urls import path
from . import views

urlpatterns = [
    # Команды проектов
    path('projects/<int:projectId>/teams', views.TeamsInProjectView.as_view()),
    path('teams/', views.TeamCreateView.as_view()),
    path('teams/<int:teamId>/', views.TeamDetailView.as_view()),
]
