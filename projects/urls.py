
from django.urls import path
from . import views

urlpatterns = [
    # Проекты
    path('projects/', views.ProjectListView.as_view()),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view()),
]
