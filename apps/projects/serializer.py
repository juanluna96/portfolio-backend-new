from rest_framework import serializers
from apps.images_projects.models import ImageProject
from apps.projects.models import Project, ProjectDescription

class ProjectDescriptionSerializer(serializers.ModelSerializer):
    language = serializers.CharField(source='language.abbreviation')
    
    class Meta:
        model = ProjectDescription
        fields = ['language', 'description']
class ProjectSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()  # Muestra el nombre del lenguaje como un campo
    images = serializers.SerializerMethodField()
    descriptions = ProjectDescriptionSerializer(many=True)  # Muestra las descripciones de cada proyecto como un campo
    categories = serializers.StringRelatedField(many=True)
    company = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'url', 'language', 'images', 'categories', 'company', 'descriptions']
        
    def get_images(self, obj):
        request = self.context.get('request')
        if request:
            # Construir la URL completa con el esquema y el dominio
            return [request.build_absolute_uri(image.image.url) for image in obj.images.all()]
        return []
    
    def get_company(self, obj):
        return obj.company.name

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProject
        fields = ['image']