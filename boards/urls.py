
from django.urls import path
from . import views

urlpatterns = [
    # Доски команд
    path('teams/<int:teamId>/boards/', views.BoardsInTeamView.as_view()),
    # Задачи
    path('boards/<int:boardId>/tasks/', views.TaskListView.as_view()),
    path('tasks/<int:taskId>/',
         views.TaskDetailView.as_view()),
    path('tasks/',
         views.AddTaskView.as_view()),
]
