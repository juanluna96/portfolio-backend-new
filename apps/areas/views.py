from rest_framework.views import APIView
from rest_framework.response import Response
from.models import Area
from .serializers import AreaSerializer
from rest_framework import status  

# Create your views here.
class AreaWithCategoriesProjectsView(APIView):
    def get(self, request, *args, **kwargs):
        language_code = request.query_params.get('language', 'en')

        areas = Area.objects.prefetch_related('categories__projects').all()

        # Serializamos las áreas, pasándole el 'language_code' al contexto de los serializers
        serializer = AreaSerializer(areas, many=True, context={'language_code': language_code})

        return Response({"areas": serializer.data}, status=status.HTTP_200_OK)
