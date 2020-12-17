from rest_framework import serializers

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        field = ("id", "name", "author")
