from rest_framework import serializers
from apps.categories.models import Category
from apps.projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'url', 'created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'color_text', 'color_bg', 'logo', 'image', 'imageBig', 'projects']
