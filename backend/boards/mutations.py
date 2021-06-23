from django.contrib.auth.models import User
from .serializers import CreateTaskSerializer
import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from .types import TaskType, StatusType
from .models import Task, Status, Board
from projects.models import Sprint


# class CreateTaskMutation(SerializerMutation):
#     class Meta:
#         serializer_class = CreateTaskSerializer


class UpdateStoryPointsMutation(graphene.Mutation):
    class Arguments:
        task_id = graphene.ID(required=True)
        story_points = graphene.Int(required=True)

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, task_id, story_points):
        task = Task.objects.get(pk=task_id)
        task.storyPoints = story_points
        task.save()

        return UpdateStoryPointsMutation(task=task)


class UpdateStatusMutation(graphene.Mutation):
    class Arguments:
        task_id = graphene.ID(required=True)
        status_id = graphene.ID(required=True)

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, task_id, status_id):
        task = Task.objects.get(pk=task_id)
        print(int(status_id) != 0)
        if int(status_id) != 0:
            status = Status.objects.get(pk=status_id)
            task.status = status
        else:
            task.status = None
        task.save()

        return UpdateStatusMutation(task=task)


class CreateStatusMutation(graphene.Mutation):
    class Arguments:
        board_id = graphene.ID(required=True)
        status_name = graphene.String(required=True)

    status = graphene.Field(StatusType)

    @classmethod
    def mutate(cls, root, info, board_id, status_name):
        board = Board.objects.get(pk=board_id)
        status = Status.objects.create(board=board, name=status_name)
        status.save()

        return CreateStatusMutation(status=status)


class CreateTaskMutation(graphene.Mutation):
    class Arguments:
        body = graphene.String(required=True)
        executor = graphene.ID()
        sprint = graphene.ID()
        status = graphene.ID()
        board = graphene.ID()
        story_points = graphene.Int()

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, body, executor, sprint, status, story_points, board):
        executorObj = User.objects.get(pk=executor)
        sprintObj = Sprint.objects.get(pk=sprint)
        statusObj = Status.objects.get(pk=status)
        boardObj = Board.objects.get(pk=board)
        task = Task.objects.create(executor=executorObj,
                                   sprint=sprintObj, status=statusObj, body=body, storyPoints=story_points, board=boardObj)
        task.save()

        return CreateTaskMutation(task=task)
