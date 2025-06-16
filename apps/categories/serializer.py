from rest_framework import serializers
from apps.categories.models import Category, CategoryDescription
from apps.projects.models import Project
from apps.languages.models import Language
from apps.projects.serializer import ProjectSerializer

class CategoryDescriptionSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()  # O un serializador completo de idioma si quieres más detalles
    
    class Meta:
        model = CategoryDescription
        fields = ['language', 'description']


class CategorySerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'color_text', 'color_bg', 'logo', 'images', 'projects', 'description', 'area_id', 'created_at', 'updated_at']

    def get_description(self, obj):
        # Obtener el idioma actual desde el contexto de la solicitud
        language_code = self.context.get('language_code', None)
        if language_code:
            language = Language.objects.filter(abbreviation=language_code).first()
            if language:
                # Obtener todas las descripciones para la categoría y el idioma
                category_descriptions = obj.descriptions.filter(language=language)
                return [desc.description for desc in category_descriptions]
        return []  # Retornar un array vacío si no hay descripciones para el idioma actual
    
    def get_images(self, obj):
        request = self.context.get('request')
        if request:
            # Construir la URL completa con el esquema y el dominio
            return {
                    'small': request.build_absolute_uri(obj.image.url),
                    'big': request.build_absolute_uri(obj.imageBig.url)
            }
        return {'small': '', 'big': ''}