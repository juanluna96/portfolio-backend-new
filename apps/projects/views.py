from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.categories.pagination import CustomPagination
from apps.projects.models import Project
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.projects.schemas import project_list_params
from apps.projects.serializer import ProjectSerializer
from django.db.models import Q


def _project_queryset():
    """Base queryset with all relations prefetched to avoid N+1."""
    return (
        Project.objects
        .select_related('company')
        .prefetch_related('language', 'images', 'categories', 'descriptions__language')
    )


class ProjectListView(APIView):
    @swagger_auto_schema(
        manual_parameters=project_list_params,
        responses={
            200: openapi.Response('List of projects', ProjectSerializer(many=True)),
            404: 'Language not found'
        }
    )
    def get(self, request, *args, **kwargs):
        locale = request.query_params.get('language', None)
        search = request.query_params.get('search', '')
        order = request.query_params.get('order', 'asc')

        projects_query = (
            _project_queryset()
            .filter(language__abbreviation=locale)
        )

        if search:
            projects_query = projects_query.filter(
                Q(descriptions__description__icontains=search) |
                Q(title__icontains=search)
            ).distinct()

        order_field = 'title' if order == 'asc' else '-title'
        projects_query = projects_query.order_by(order_field)

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(projects_query, request, view=self)

        if result_page is not None:
            serializer = ProjectSerializer(result_page, many=True, context={'request': request})
            return paginator.get_paginated_response({'projects': serializer.data})

        serializer = ProjectSerializer(projects_query, many=True, context={'request': request})
        return Response({'projects': serializer.data}, status=status.HTTP_200_OK)
