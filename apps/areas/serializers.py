from apps.areas.models import Area
from apps.categories.serializer import CategorySerializer
from rest_framework import serializers

class AreaSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Area
        fields = ['title', 'name', 'logo', 'categories']