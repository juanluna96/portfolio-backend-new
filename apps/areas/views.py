from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Area
from .serializers import AreaSerializer
from rest_framework import status
from django.db.models import Prefetch
from apps.categories.models import Category
from apps.projects.models import Project


class AreaWithCategoriesProjectsView(APIView):
    def get(self, request, *args, **kwargs):
        language_code = request.query_params.get('language', 'en')

        projects_qs = (
            Project.objects.order_by('title')
            .select_related('company')
            .prefetch_related('language', 'images', 'descriptions')
        )
        categories_qs = Category.objects.order_by('name').prefetch_related(
            Prefetch('projects', queryset=projects_qs)
        )
        areas = Area.objects.order_by('title').prefetch_related(
            Prefetch('categories', queryset=categories_qs)
        )

        serializer = AreaSerializer(areas, many=True, context={'language_code': language_code, 'request': request})

        return Response({"areas": serializer.data}, status=status.HTTP_200_OK)
