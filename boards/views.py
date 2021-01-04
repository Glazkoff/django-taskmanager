from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Board, Project, Task, Team
from .serializers import BoardsInTeamSerializer, CreateTaskSerializer, ProjectListSerializer, ProjectDetailSerializer, TaskDetailSerializer, TaskListSerializer, TeamCreateSerializer, TeamsInProjectSerializer


class ProjectListView(APIView):
    """Вывод списка проектов"""

    def get(self, request):
        projects = Project.objects.filter(draft=False)
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetailView(APIView):
    """Вывод проекта"""

    def get(self, request, pk):
        project = Project.objects.get(id=pk, draft=False)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)


class AddTaskView(APIView):
    """Добавление задачи в доску"""

    def post(self, request):
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)


class TaskDetailView(APIView):
    """Задача в таблице"""

    def get(self, request, boardId, taskId):
        try:
            task = Task.objects.get(id=taskId)
            serializer = TaskDetailSerializer(task, many=False)
            return Response(serializer.data)
        except Task.DoesNotExist:
            task = None
            return Response({})


class TaskListView(APIView):
    """Список задач в таблице"""

    def get(self, request, boardId):
        tasks = Task.objects.filter(board=boardId)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, boardId):
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(board=boardId)
            return Response(status=201)
        else:
            return Response(status=400)


class TeamsInProjectView(APIView):
    """Команды в проекте"""

    def get(self, request, projectId):
        try:
            teams = Team.objects.filter(project=projectId)
            serializer = TeamsInProjectSerializer(teams, many=True)
            return Response(serializer.data)
        except Team.DoesNotExist:
            return Response([])


class TeamCreateView(APIView):
    """Добавление команды"""

    def post(self, request):
        team = TeamCreateSerializer(data=request.data)
        if team.is_valid():
            team.save()
        return Response(status=201)


class BoardsInTeamView(APIView):
    """Список досок у команды"""

    def get(self, request, teamId):
        try:
            boards = Board.objects.filter(team=teamId)
            serializer = BoardsInTeamSerializer(boards, many=True)
            return Response(serializer.data)
        except Board.DoesNotExist:
            return Response([])
