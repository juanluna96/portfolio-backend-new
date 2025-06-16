from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.categories.models import Category
from apps.categories.pagination import CustomPagination
from apps.languages.models import Language
from apps.categories.serializer import CategorySerializer, ProjectSerializer
from rest_framework.pagination import PageNumberPagination

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.categories.schemas import (
    category_list_by_language_params,
    categories_description_with_all_languages_params,
    category_projects_view_params,
)

class CategoryListByLanguage(APIView):

    @swagger_auto_schema(manual_parameters=category_list_by_language_params, responses={
        200: openapi.Response('Success', CategorySerializer(many=True)),
        400: 'Language parameter is required',
        404: 'Language not found'
    })
    def get(self, request, *args, **kwargs):
        locale = request.query_params.get('language', None)
        
        if locale is None:
            return Response({"detail": "Language parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Obtener el lenguaje que coincide con el 'locale'
        language = Language.objects.filter(abbreviation=locale).first()
        
        if not language:
            return Response({"detail": "Language not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Obtener todas las categorías que tienen proyectos con el lenguaje especificado
        categories_with_projects = Category.objects.filter(
            projects__language=language
        ).distinct()

        # Serializamos las categorías y las devolvemos
        serializer = CategorySerializer(categories_with_projects, many=True, context={'request': request})
        return Response({"categories": serializer.data}, status=status.HTTP_200_OK)

class CategoriesDescriptionWithAllLanguages(APIView):
    
    @swagger_auto_schema(manual_parameters=categories_description_with_all_languages_params, responses={
        200: openapi.Response('Success', CategorySerializer()),
        404: 'Language not found or invalid language specified'
    })
    def get(self, request, *args, **kwargs):
        # Obtén el idioma actual
        locale = request.query_params.get('language', None)

        if locale is None:
            return Response({"detail": "Language not found"}, status=status.HTTP_404_NOT_FOUND)
        
        language = Language.objects.filter(abbreviation=locale).first()
        
        if not language:
            return Response({"detail": "Invalid language specified"}, status=status.HTTP_404_NOT_FOUND)
        
        # Obtén el parámetro de categoría si está presente
        category_param = request.query_params.get('category', None)

        if category_param:
            # Filtra por una categoría específica si se pasa el parámetro
            category = Category.objects.filter(id=category_param).prefetch_related('descriptions__language').first()
            if not category:
                return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
            
            # Verifica si la categoría tiene una descripción en el idioma actual
            category_description = category.descriptions.filter(language=language).first()
            if category_description:
                category.description_in_current_language = category_description.description
                serializer = CategorySerializer(category, context={'language_code': locale, 'request': request})
                return Response({"category": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Category description not found for the specified language"}, status=status.HTTP_404_NOT_FOUND)

        # Obtener todas las categorías con las descripciones en el idioma actual
        categories = Category.objects.all().prefetch_related('descriptions__language')

        # Filtramos las categorías que tienen descripciones en el idioma solicitado
        filtered_categories = []
        for category in categories:
            category_description = category.descriptions.filter(language=language).first()
            if category_description:
                category.description_in_current_language = category_description.description
                filtered_categories.append(category)

        # Serializamos las categorías
        serializer = CategorySerializer(filtered_categories, many=True, context={'language_code': locale, 'request': request})

        return Response({"categories": serializer.data}, status=status.HTTP_200_OK)
    
class CategoryProjectsView(APIView):
    
    @swagger_auto_schema(manual_parameters=category_projects_view_params)
    def get(self, request, *args, **kwargs):
        # Obtener parámetros de la query
        locale = request.query_params.get('language', None)
        category = request.query_params.get('category', None)

        if not locale or not category:
            return Response({"detail": "Both 'language' and 'category' parameters are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Obtener el lenguaje y la categoría
        try:
            language = Language.objects.get(abbreviation=locale)
            category = Category.objects.get(id=category) if category.isdigit() else Category.objects.get(name__iexact=category)
        except Language.DoesNotExist:
            return Response({"detail": "Language not found"}, status=status.HTTP_404_NOT_FOUND)
        except Category.DoesNotExist:
            return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        # Filtrar proyectos relacionados con la categoría y el lenguaje especificado
        projects = category.projects.filter(language__abbreviation=language.abbreviation)

        # Configurar paginación
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(projects, request)

        # Serializar los proyectos
        serializer = ProjectSerializer(result_page, many=True, context={'request': request})

        return paginator.get_paginated_response({"category": category.name, "projects": serializer.data})