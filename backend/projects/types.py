from graphene_django.types import DjangoObjectType
from .models import Project, ProjectSettings, Sprint


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectSettingsType(DjangoObjectType):
    class Meta:
        model = ProjectSettings
        fields = '__all__'


class SprintType(DjangoObjectType):
    class Meta:
        model = Sprint
        fields = '__all__'
