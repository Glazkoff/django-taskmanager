import graphene
from .models import Team, Employee
from .types import TeamType, EmployeeType


class Query(graphene.ObjectType):
    teams = graphene.List(TeamType)
    team = graphene.Field(TeamType, team_id=graphene.ID())
    employees = graphene.List(EmployeeType)
    employee = graphene.Field(EmployeeType, employee_id=graphene.ID())

    def resolve_teams(self, info, **kwargs):
        return Team.objects.all()

    def resolve_team(self, info, team_id):
        return Team.objects.get(pk=team_id)

    def resolve_employees(self, info, **kwargs):
        return Employee.objects.all()

    def resolve_employee(self, info, employee_id):
        return Employee.objects.get(pk=employee_id)


schema = graphene.Schema(query=Query,)
