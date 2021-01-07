
from django.urls import path
from . import views

urlpatterns = [
    # Доски команд
    path('teams/<int:teamId>/boards/', views.BoardsInTeamView.as_view()),
    # Задачи
    path('board/<int:boardId>/tasks/', views.TaskListView.as_view()),
    path('board/<int:boardId>/tasks/<int:taskId>/',
         views.TaskDetailView.as_view()),
]
