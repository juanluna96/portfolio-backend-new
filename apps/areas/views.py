from rest_framework.views import APIView
from rest_framework.response import Response
from.models import Area
from .serializers import AreaSerializer
from rest_framework import status  

# Create your views here.
class AreaWithCategoriesProjectsView(APIView):
    def get(self, request, *args, **kwargs):
        areas = Area.objects.prefetch_related('categories__project_set').all()  # Usamos prefetch_related para obtener las categorías con sus proyectos

        # Serializamos las áreas con categorías y proyectos
        serializer = AreaSerializer(areas, many=True)

        return Response({"areas": serializer.data}, status=status.HTTP_200_OK)
