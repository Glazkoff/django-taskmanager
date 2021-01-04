
from django.urls import path
from . import views

urlpatterns = [
    # Проекты
    path('projects/', views.ProjectListView.as_view()),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view()),
    # Команды проектов
    path('projects/<int:projectId>/teams', views.TeamsInProjectView.as_view()),
    path('teams/', views.TeamCreateView.as_view()),
    # Доски команд
    path('teams/<int:teamId>/boards/', views.BoardsInTeamView.as_view()),
    # Задачи
    path('board/<int:boardId>/tasks/', views.TaskListView.as_view()),
    path('board/<int:boardId>/tasks/<int:taskId>/',
         views.TaskDetailView.as_view()),

]
