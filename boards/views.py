from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer, TeamCreateSerializer


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


class TeamCreateView(APIView):
    """Добавление команды"""

    def post(self, request):
        team = TeamCreateSerializer(data=request.data)
        if team.is_valid():
            team.save()
        return Response(status=201)
