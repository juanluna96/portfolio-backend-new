from rest_framework import serializers
from apps.companies.serializers import CompanySerializer
from apps.images_projects.models import ImageProject
from apps.projects.models import Project, ProjectDescription

class ProjectDescriptionSerializer(serializers.ModelSerializer):
    language = serializers.CharField(source='language.abbreviation')
    
    class Meta:
        model = ProjectDescription
        fields = ['language', 'description']
class ProjectSerializer(serializers.ModelSerializer):
    language = serializers.SerializerMethodField()  # Muestra el nombre del lenguaje como un campo
    images = serializers.SerializerMethodField()
    descriptions = ProjectDescriptionSerializer(many=True)  # Muestra las descripciones de cada proyecto como un campo
    categories = serializers.SerializerMethodField()  # Muestra las categorías de cada proyecto como un campo
    company = CompanySerializer()

    class Meta:
        model = Project
        fields = ['id', 'title', 'url', 'language', 'images', 'categories', 'company', 'descriptions']
        
    def get_images(self, obj):
        request = self.context.get('request')
        if request:
            seen = set()
            result = []
            for image in obj.images.all():
                url = request.build_absolute_uri(image.image.url)
                if url not in seen:
                    seen.add(url)
                    result.append(url)
            return result
        return []

    def get_company(self, obj):
        return obj.company.name

    def get_language(self, obj):
        seen = set()
        result = []
        for language in obj.language.all():
            if language.abbreviation not in seen:
                seen.add(language.abbreviation)
                result.append(language.abbreviation)
        return result

    def get_categories(self, obj):
        request = self.context.get('request')
        seen = set()
        result = []
        for category in obj.categories.all().order_by('name'):
            if category.id not in seen:
                seen.add(category.id)
                result.append({
                    'id': category.id,
                    'name': category.name,
                    'logo': category.logo,
                    'color_bg': category.color_bg,
                    'color_text': category.color_text,
                    'images': {
                        'small': request.build_absolute_uri(category.image.url),
                        'big': request.build_absolute_uri(category.imageBig.url),
                    },
                })
        return result

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProject
        fields = ['image']