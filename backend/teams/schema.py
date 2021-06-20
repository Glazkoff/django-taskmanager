import graphene
from .models import Team, Employee
from .types import TeamType, EmployeeType


class Query(graphene.ObjectType):
    teams = graphene.List(TeamType)
    team = graphene.Field(TeamType, team_id=graphene.ID())

    def resolve_teams(self, info, **kwargs):
        return Team.objects.all()

    def resolve_team(self, info, team_id):
        return Team.objects.get(pk=team_id)


schema = graphene.Schema(query=Query,)
