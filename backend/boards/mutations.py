import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from .types import TaskType
from .models import Task, Status
from .serializers import CreateTaskSerializer


class CreateTaskMutation(SerializerMutation):
    class Meta:
        serializer_class = CreateTaskSerializer


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
