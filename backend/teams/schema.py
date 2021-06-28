import graphene
from .models import Team, Employee
from django.contrib.auth.models import User
from .types import TeamType, EmployeeType, UserType


class Query(graphene.ObjectType):
    teams = graphene.List(TeamType)
    team = graphene.Field(TeamType, team_id=graphene.ID())
    employees = graphene.List(EmployeeType)
    employee = graphene.Field(EmployeeType, employee_id=graphene.ID())
    users = graphene.List(UserType)

    def resolve_teams(self, info, **kwargs):
        return Team.objects.all()

    def resolve_team(self, info, team_id):
        return Team.objects.get(pk=team_id)

    def resolve_employees(self, info, **kwargs):
        return Employee.objects.all()

    def resolve_employee(self, info, employee_id):
        return Employee.objects.get(pk=employee_id)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


schema = graphene.Schema(query=Query,)
