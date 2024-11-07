from rest_framework import serializers
from apps.images_projects.models import ImageProject
from apps.projects.models import Project, ProjectDescription

class ProjectDescriptionSerializer(serializers.ModelSerializer):
    language = serializers.CharField(source='language.name')
    
    class Meta:
        model = ProjectDescription
        fields = ['language', 'description']
class ProjectSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()  # Muestra el nombre del lenguaje como un campo
    images = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)
    company = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'url', 'language', 'images', 'categories', 'company', 'created_at', 'updated_at']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProject
        fields = ['image']