from .models import Team
from rest_framework import serializers

# Работа с командами


class TeamCreateSerializer(serializers.ModelSerializer):
    """Команда"""
    class Meta:
        model = Team
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    """Вывод команды"""
    class Meta:
        model = Team
        fields = ("name", "leader", "project", "participants")


class TeamsInProjectSerializer(serializers.ModelSerializer):
    """Команды в проекте"""
    class Meta:
        model = Team
        exclude = ("project",)
