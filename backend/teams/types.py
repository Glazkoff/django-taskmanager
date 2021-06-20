from graphene_django.types import DjangoObjectType
from .models import Team, Employee


class TeamType(DjangoObjectType):
    class Meta:
        model = Team
        fields = '__all__'


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = '__all__'
