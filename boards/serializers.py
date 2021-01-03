from django.db.models import fields
from django.urls.conf import include
from rest_framework import serializers

from .models import Project, Team


class ProjectListSerializer(serializers.ModelSerializer):
    """Список проектов"""
    leader = serializers.SlugRelatedField(
        slug_field="username", read_only=True)

    class Meta:
        model = Project
        fields = ("id", "name", "leader")


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


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Полный проект"""
    leader = serializers.SlugRelatedField(
        slug_field="username", read_only=True)
    teams = TeamSerializer(many=True)

    class Meta:
        model = Project
        exclude = ("draft",)
