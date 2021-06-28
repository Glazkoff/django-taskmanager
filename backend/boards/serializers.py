from django.db.models import fields
from django.urls.conf import include
from rest_framework import serializers

from .models import Board, Comment, Task


# Работа с досками

class BoardsInTeamSerializer(serializers.ModelSerializer):
    """Список досок в команде"""

    class Meta:
        model = Board
        exclude = ("team",)

# Комментарии


class FilterCommentsSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.ModelSerializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentsSerializer(serializers.ModelSerializer):
    """Комментарии задачи"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentsSerializer
        model = Comment
        fields = ("id", "children", "body")


# Работа с задачами

class CreateTaskSerializer(serializers.ModelSerializer):
    """Добавление задачи"""
    class Meta:
        model = Task
        fields = ("executor", "storyPoints", "body", "board")

    def create(self, validated_data):
        return Task.objects.update_or_create(
            executor=validated_data.get("executor", None),
            board=validated_data.get("board", None),
            body=validated_data.get("body", None),
            defaults={"storyPoints": validated_data.get("storyPoints", None)})


class TaskDetailSerializer(serializers.ModelSerializer):
    """Задача на доске"""
    class Meta:
        model = Task
        exclude = ("board",)


class TaskListSerializer(serializers.ModelSerializer):
    """Список задач"""
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ("id", "storyPoints", "body", "executor",
                  "sprint", "status", "comments")
