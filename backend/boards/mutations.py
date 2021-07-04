from django.contrib.auth.models import User
from .serializers import CreateTaskSerializer
import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from .types import TaskType, StatusType, BoardType
from teams.types import TeamType, UserType, EmployeeType
from projects.types import ProjectType, SprintType
from .models import Task, Status, Board
from projects.models import Sprint, Project
from teams.models import Team, Employee
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404


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


class CreateStatusMutation(graphene.Mutation):
    class Arguments:
        board_id = graphene.ID(required=True)
        status_name = graphene.String(required=True)

    status = graphene.Field(StatusType)

    @classmethod
    def mutate(cls, root, info, board_id, status_name):
        board = Board.objects.get(pk=board_id)
        status = Status.objects.create(board=board, name=status_name)
        status.save()

        return CreateStatusMutation(status=status)


class DeleteStatusMutation(graphene.Mutation):
    class Arguments:
        status_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, status_id):
        status = Status.objects.get(pk=status_id)
        status.delete()

        return cls(ok=True)


class CreateTaskMutation(graphene.Mutation):
    class Arguments:
        body = graphene.String(required=True)
        executor = graphene.ID()
        sprint = graphene.ID()
        status = graphene.ID()
        board = graphene.ID()
        story_points = graphene.Int()

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, body, executor, sprint, story_points, board, status=None):
        executorObj = User.objects.get(pk=executor)
        sprintObj = Sprint.objects.get(pk=sprint)
        boardObj = Board.objects.get(pk=board)
        statusObj = None
        if status is None or status == 0:
            statusObj = Status.objects.get(pk=status)
        task = Task.objects.create(executor=executorObj, sprint=sprintObj,
                                   status=statusObj, body=body, storyPoints=story_points, board=boardObj)
        task.save()

        return CreateTaskMutation(task=task)


class UpdateTaskMutation(graphene.Mutation):
    class Arguments:
        task_id = graphene.ID(required=True)
        body = graphene.String(required=True)
        executor = graphene.ID()
        sprint = graphene.ID()
        status = graphene.ID()
        story_points = graphene.Int()

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, body, story_points, task_id, sprint=None, executor=None, status=None):
        task = Task.objects.get(pk=task_id)

        if (status != None):
            statusObj = Status.objects.get(pk=status)
            task.status = statusObj
        if (executor != None):
            executorObj = User.objects.get(pk=executor)
            task.executor = executorObj
        if (sprint != None):
            sprintObj = Sprint.objects.get(pk=sprint)
            task.sprint = sprintObj
        task.body = body
        task.storyPoints = story_points
        task.save()

        return UpdateTaskMutation(task=task)


class CreateBoardMutation(graphene.Mutation):
    class Arguments:
        team_id = graphene.ID(required=True)
        name = graphene.String(required=True)

    board = graphene.Field(BoardType)

    @classmethod
    def mutate(cls, root, info, team_id, name):
        team = Team.objects.get(pk=team_id)
        board = Board.objects.create(team=team, name=name)
        board.save()

        return CreateBoardMutation(board=board)


class CreateTeamMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        leader_id = graphene.ID(required=True)
        project_id = graphene.ID(required=True)
        participants = graphene.List(graphene.ID)

    team = graphene.Field(TeamType)

    @classmethod
    def mutate(cls, root, info, name, leader_id, project_id, participants):
        nameObj = name
        leaderObj = User.objects.get(pk=leader_id)
        projectObj = Project.objects.get(pk=project_id)
        participantsObj = User.objects.filter(pk__in=participants)
        team = Team.objects.create(
            name=nameObj, leader=leaderObj, project=projectObj)
        team.participants.set(participantsObj)
        team.save()
        return CreateTeamMutation(team=team)


class CreateProjectMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        prefix = graphene.String(required=True)
        draft = graphene.Boolean()
        leader_id = graphene.ID(required=True)
        teams = graphene.List(graphene.ID)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, leader_id, name, prefix, teams, draft=False):
        leader = User.objects.get(pk=leader_id)
        project = Project.objects.create(
            name=name, prefix=prefix, draft=draft, leader=leader)
        teams = Team.objects.filter(id__in=teams)
        project.teams.set(teams)
        project.save()

        return CreateProjectMutation(project=project)


class CreateSprintMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        aim = graphene.String(required=True)
        project_id = graphene.ID(required=True)
        start_date = graphene.String()
        finish_date = graphene.String()

    sprint = graphene.Field(SprintType)

    @classmethod
    def mutate(cls, root, info, name, aim, project_id, start_date=None, finish_date=None):
        projectObj = Project.objects.get(pk=project_id)
        sprint = Sprint.objects.create(
            name=name, aim=aim, project=projectObj, startDate=start_date, finishDate=finish_date)

        return CreateSprintMutation(sprint=sprint)


class CreateProjectMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        prefix = graphene.String(required=True)
        draft = graphene.Boolean()
        leader_id = graphene.ID(required=True)
        teams = graphene.List(graphene.ID)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, leader_id, name, prefix, teams, draft=False):
        leader = User.objects.get(pk=leader_id)
        project = Project.objects.create(
            name=name, prefix=prefix, draft=draft, leader=leader)
        teams = Team.objects.filter(id__in=teams)
        project.teams.set(teams)
        project.save()

        return CreateProjectMutation(project=project)


class CreateUserAuthMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType)
    employee = graphene.Field(EmployeeType)
    is_ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info,  username, password):
        try:
            user = User.objects.get(username=username)
            is_ok = check_password(password, user.password)
            if not is_ok:
                return CreateUserAuthMutation(user=None, employee=None, is_ok=is_ok)
            employee = Employee.objects.get(user=user)
            return CreateUserAuthMutation(user=user, employee=employee, is_ok=is_ok)
        except User.DoesNotExist:
            user = None
            return CreateUserAuthMutation(user=None, employee=None, is_ok=False)
