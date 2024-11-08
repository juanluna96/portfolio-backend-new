from rest_framework import serializers
from .models import Biography

class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'