from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.categories.models import Category
from apps.languages.models import Language
from apps.categories.serializer import CategorySerializer

class CategoryListByLanguage(APIView):
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
            project__language=language
        ).distinct()

        # Serializamos las categorías y las devolvemos
        serializer = CategorySerializer(categories_with_projects, many=True)
        return Response({"categories": serializer.data}, status=status.HTTP_200_OK)
