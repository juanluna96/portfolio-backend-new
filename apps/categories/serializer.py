from rest_framework import serializers
from apps.categories.models import Category, CategoryDescription
from apps.projects.models import Project
from apps.languages.models import Language
from apps.projects.serializer import ProjectImageSerializer

class CategoryDescriptionSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()  # O un serializador completo de idioma si quieres más detalles
    
    class Meta:
        model = CategoryDescription
        fields = ['language', 'description']
class ProjectSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = ['title', 'description', 'url', 'created_at', 'updated_at', 'images']
        
    def get_images(self, obj):
        request = self.context.get('request')
        if request:
            # Construir la URL completa con el esquema y el dominio
            return [request.build_absolute_uri(image.image.url) for image in obj.images.all()]
        return []


class CategorySerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'color_text', 'color_bg', 'logo', 'image', 'imageBig', 'projects', 'description', 'area_id', 'created_at', 'updated_at']

    def get_description(self, obj):
        # Obtener el idioma actual desde la solicitud
        language_code = self.context.get('language_code', None)
        if language_code:
            language = Language.objects.filter(abbreviation=language_code).first()
            if language:
                category_description = obj.descriptions.filter(language=language).first()
                if category_description:
                    return category_description.description
        return None  # Si no hay descripción para el idioma actual