from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Prefetch
from apps.categories.models import Category, CategoryDescription
from apps.categories.pagination import CustomPagination
from apps.languages.models import Language
from apps.categories.serializer import CategorySerializer, ProjectSerializer
from apps.projects.models import Project

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.categories.schemas import (
    category_list_by_language_params,
    categories_description_with_all_languages_params,
    category_projects_view_params,
)


def _project_queryset():
    return (
        Project.objects
        .select_related('company')
        .prefetch_related('language', 'images', 'categories', 'descriptions__language')
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

        language = Language.objects.filter(abbreviation=locale).first()
        if not language:
            return Response({"detail": "Language not found"}, status=status.HTTP_404_NOT_FOUND)

        categories_with_projects = (
            Category.objects
            .filter(projects__language=language)
            .distinct()
            .prefetch_related(
                Prefetch('projects', queryset=_project_queryset()),
                Prefetch(
                    'descriptions',
                    queryset=CategoryDescription.objects.filter(language=language),
                    to_attr='descriptions_for_lang',
                ),
            )
        )

        serializer = CategorySerializer(
            categories_with_projects, many=True,
            context={'request': request, 'language_code': locale},
        )
        return Response({"categories": serializer.data}, status=status.HTTP_200_OK)


class CategoriesDescriptionWithAllLanguages(APIView):

    @swagger_auto_schema(manual_parameters=categories_description_with_all_languages_params, responses={
        200: openapi.Response('Success', CategorySerializer()),
        404: 'Language not found or invalid language specified'
    })
    def get(self, request, *args, **kwargs):
        locale = request.query_params.get('language', None)

        if locale is None:
            return Response({"detail": "Language not found"}, status=status.HTTP_404_NOT_FOUND)

        language = Language.objects.filter(abbreviation=locale).first()
        if not language:
            return Response({"detail": "Invalid language specified"}, status=status.HTTP_404_NOT_FOUND)

        category_param = request.query_params.get('category', None)

        if category_param:
            category = (
                Category.objects
                .filter(id=category_param)
                .prefetch_related(
                    Prefetch(
                        'descriptions',
                        queryset=CategoryDescription.objects.filter(language=language),
                        to_attr='descriptions_for_lang',
                    )
                )
                .first()
            )
            if not category:
                return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

            if not category.descriptions_for_lang:
                return Response(
                    {"detail": "Category description not found for the specified language"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = CategorySerializer(category, context={'language_code': locale, 'request': request})
            return Response({"category": serializer.data}, status=status.HTTP_200_OK)

        # Prefetch only the descriptions for the requested language — one extra query instead of N.
        categories = Category.objects.prefetch_related(
            Prefetch(
                'descriptions',
                queryset=CategoryDescription.objects.filter(language=language),
                to_attr='descriptions_for_lang',
            )
        )

        # Filter in Python on already-prefetched data — zero extra DB queries.
        filtered_categories = [c for c in categories if c.descriptions_for_lang]

        serializer = CategorySerializer(
            filtered_categories, many=True,
            context={'language_code': locale, 'request': request},
        )
        return Response({"categories": serializer.data}, status=status.HTTP_200_OK)


class CategoryProjectsView(APIView):

    @swagger_auto_schema(manual_parameters=category_projects_view_params)
    def get(self, request, *args, **kwargs):
        locale = request.query_params.get('language', None)
        category_param = request.query_params.get('category', None)

        if not locale or not category_param:
            return Response(
                {"detail": "Both 'language' and 'category' parameters are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            if category_param.isdigit():
                category = Category.objects.get(id=category_param)
            else:
                category = Category.objects.get(name__iexact=category_param)
        except Category.DoesNotExist:
            return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        projects = (
            _project_queryset()
            .filter(categories=category, language__abbreviation=locale)
        )

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(projects, request)

        serializer = ProjectSerializer(result_page, many=True, context={'request': request})
        return paginator.get_paginated_response({"category": category.name, "projects": serializer.data})
