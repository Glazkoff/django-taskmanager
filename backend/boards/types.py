import graphene
from graphene_django.types import DjangoObjectType
from .models import Board, Task, Status, Comment


class BoardType(DjangoObjectType):
    tasks_count = graphene.Int()

    class Meta:
        model = Board
        fields = '__all__'

    def resolve_tasks_count(self, info):
        return self.task_set.count()


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
