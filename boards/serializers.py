from django.db.models import fields
from django.urls.conf import include
from rest_framework import serializers

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    """Список проектов"""
    leader = serializers.SlugRelatedField(
        slug_field="username", read_only=True)

    class Meta:
        model = Project
        fields = ("id", "name", "leader")


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Полный проект"""
    leader = serializers.SlugRelatedField(
        slug_field="username", read_only=True)

    class Meta:
        model = Project
        exclude = ("draft",)
