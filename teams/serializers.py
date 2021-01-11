from django.contrib.auth.models import User
from .models import Team
from rest_framework import serializers

# Работа с командами


class TeamCreateSerializer(serializers.ModelSerializer):
    """Команда"""
    class Meta:
        model = Team
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """Вывод пользователя"""
    class Meta:
        model = User
        fields = ("id", "username", "first_name",
                  "last_name", "is_staff", "employee")


class TeamDetailSerializer(serializers.ModelSerializer):
    """Вывод команды"""
    participants = UserSerializer(many=True,  read_only=True)

    class Meta:
        model = Team
        fields = ("name", "leader", "project", "participants")


class TeamsInProjectSerializer(serializers.ModelSerializer):
    """Команды в проекте"""
    class Meta:
        model = Team
        exclude = ("project",)
