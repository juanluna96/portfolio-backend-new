from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.languages.models import Language
from apps.languages.serializer import LanguageSerializer

class LanguageListView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener todos los lenguajes
        languages = Language.objects.all()
        
        # Serializar los lenguajes
        serializer = LanguageSerializer(languages, many=True)
        
        # Retornar la respuesta en formato JSON
        return Response(serializer.data, status=status.HTTP_200_OK)
