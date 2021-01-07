from .serializers import TeamCreateSerializer, TeamsInProjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Team


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
