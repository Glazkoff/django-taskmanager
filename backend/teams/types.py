import graphene
from graphene_django.types import DjangoObjectType
from .models import Team, Employee
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = '__all__'


class TeamType(DjangoObjectType):
    participants = graphene.List(EmployeeType)

    class Meta:
        model = Team
        fields = '__all__'

    def resolve_participants(self, info):
        ids = [participant.id for participant in self.participants.all()]
        return Employee.objects.filter(user__pk__in=ids)
