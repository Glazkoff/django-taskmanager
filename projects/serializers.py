from rest_framework import serializers
from .models import Project
from teams.serializers import TeamSerializer

# Работа с проектами


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Полный проект"""
    leader = serializers.SlugRelatedField(
        slug_field="username", read_only=True)
    teams = TeamSerializer(many=True)

    class Meta:
        model = Project
        exclude = ("draft",)


class ProjectListSerializer(serializers.ModelSerializer):
    """Список проектов"""
    leader = serializers.SlugRelatedField(
        slug_field="username", read_only=True)

    class Meta:
        model = Project
        fields = ("id", "name", "leader")
