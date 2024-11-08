from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Biography
from .serializer import BiographySerializer

class LastBiographyView(APIView):
    def get(self, request):
        last_biography = Biography.objects.last()  # Obtiene la última biografía registrada
        if last_biography:
            serializer = BiographySerializer(last_biography)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No biography found'}, status=status.HTTP_404_NOT_FOUND)
