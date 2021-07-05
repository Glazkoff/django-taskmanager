import graphene
from collections import namedtuple
from .models import Project, ProjectSettings, Sprint
from boards.models import Board
from .types import ProjectType, ProjectSettingsType, SprintType
from teams.types import TeamType
from teams.models import Team
from django.db.models import Sum, Count

ProjectStatisticsObject = namedtuple(
    "ProjectStatisticsType", ["teams_count", "sprints_count", "status_average", "teams"])


class ProjectStatisticsType(graphene.ObjectType):
    teams_count = graphene.Int()
    sprints_count = graphene.Int()
    status_average = graphene.Float()
    teams = graphene.List(TeamType)


class Query(graphene.ObjectType):
    projects = graphene.List(ProjectType)
    project = graphene.Field(ProjectType, project_id=graphene.ID())
    projects_settings = graphene.List(ProjectSettingsType)
    project_settings = graphene.Field(
        ProjectSettingsType, project_settings_id=graphene.ID())
    sprints = graphene.List(SprintType)
    sprint = graphene.Field(SprintType, sprint_id=graphene.ID())
    statistics = graphene.Field(
        ProjectStatisticsType, project_id=graphene.ID())

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

    def resolve_statistics(self, info, project_id):
        project = Project.objects\
            .annotate(teams_count=Count('teams', distinct=True))\
            .annotate(sprints_count=Count('sprint', distinct=True))\
            .get(pk=project_id)
        teams = Team.objects.annotate(boards_count=Count(
            'board', distinct=True)).filter(project=project.id)
        boards_count = 0
        status_count = 0
        for team in teams:
            boards = Board.objects.annotate(status_count=Count(
                'status', distinct=True)).annotate(tasks_count=Count(
                    'task', distinct=True)).filter(team=team.id)
            for board in boards:
                boards_count += 1
                status_count += board.status_count+1
        average_status_count = status_count / boards_count if boards_count != 0 else 0
        return ProjectStatisticsObject(teams_count=project.teams_count, sprints_count=project.sprints_count, status_average=average_status_count, teams=teams)


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query,)
