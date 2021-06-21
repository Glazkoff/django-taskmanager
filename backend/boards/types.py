from graphene_django.types import DjangoObjectType
from .models import Board, Task, Status, Comment
from projects.models import Sprint


class SprintType(DjangoObjectType):
    class Meta:
        model = Sprint
        fields = '__all__'


class BoardType(DjangoObjectType):
    class Meta:
        model = Board
        fields = '__all__'


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = '__all__'


class StatusType(DjangoObjectType):
    class Meta:
        model = Status
        fields = '__all__'


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = '__all__'
