import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from .types import Task
from .models import Task
from .serializers import CreateTaskSerializer


class CreateTaskMutation(SerializerMutation):
    class Meta:
        serializer_class = CreateTaskSerializer
