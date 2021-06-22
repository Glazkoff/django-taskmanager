import graphene
from .models import Project, ProjectSettings, Sprint
from .types import ProjectType, ProjectSettingsType, SprintType


class Query(graphene.ObjectType):
    projects = graphene.List(ProjectType)
    project = graphene.Field(ProjectType, project_id=graphene.ID())
    projects_settings = graphene.List(ProjectSettingsType)
    project_settings = graphene.Field(
        ProjectSettingsType, project_settings_id=graphene.ID())
    sprints = graphene.List(SprintType)
    sprint = graphene.Field(SprintType, sprint_id=graphene.ID())

    def resolve_projects(self, info, **kwargs):
        return Project.objects.all()

    def resolve_project(self, info, project_id):
        return Project.objects.get(pk=project_id)

    def resolve_projects_settings(self, info, **kwargs):
        return ProjectSettings.objects.all()

    def resolve_project_settings(self, info, project_settings_id):
        return ProjectSettings.objects.get(pk=project_settings_id)

    def resolve_sprints(self, info, **kwargs):
        return Sprint.objects.all()

    def resolve_sprint(self, info, sprint_id):
        return Sprint.objects.get(pk=sprint_id)


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query,)
