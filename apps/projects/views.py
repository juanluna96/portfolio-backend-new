from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.languages.models import Language
from apps.projects.models import Project
from apps.projects.schemas import ProjectListSchema
from apps.projects.serializer import ProjectSerializer
from django.db.models import Q

class ProjectListView(APIView):
    schema = ProjectListSchema()
    def get(self, request, *args, **kwargs):
        locale = request.query_params.get('language', None)
        search = request.query_params.get('search', '')
        order = request.query_params.get('order', 'asc')

        try:
            language = Language.objects.get(abbreviation=locale)
        except Language.DoesNotExist:
            return Response({'error': 'Language not found'}, status=status.HTTP_404_NOT_FOUND)

        # Filtra proyectos relacionados con el lenguaje
        projects_query = Project.objects.filter(language=language)

        if search:
            projects_query = projects_query.filter(
                Q(descriptions__description__icontains=search) |
                Q(title__icontains=search)
            ).distinct()

        # Ordenar por título, por defecto ascendente
        order_field = 'title' if order == 'asc' else '-title'
        projects_query = projects_query.order_by(order_field)

        # Serializa y devuelve los proyectos
        serializer = ProjectSerializer(projects_query, many=True)
        return Response({'projects': serializer.data}, status=status.HTTP_200_OK)
