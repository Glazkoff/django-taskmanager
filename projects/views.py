from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer


class ProjectListView(APIView):
    """Вывод списка проектов"""

    def get(self, request):
        projects = Project.objects.filter(draft=False)
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetailView(APIView):
    """Вывод проекта"""

    def get(self, request, pk):
        try:
            project = Project.objects.get(id=pk, draft=False)
            serializer = ProjectDetailSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            # запросу не соответствует ни один элемент.
            return Response({})
        except Project.MultipleObjectsReturned:
            # запросу соответствует несколько элементов.
            return Response({})
