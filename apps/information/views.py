from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Biography
from .serializer import BiographySerializer


class LastBiographyView(APIView):
    def get(self, request):
        language = request.query_params.get('language', 'en')
        last_biography = Biography.objects.last()
        if last_biography:
            serializer = BiographySerializer(last_biography, context={'language': language})
            response = Response(serializer.data, status=status.HTTP_200_OK)
            response['Cache-Control'] = 'public, max-age=300'
            return response
        return Response({'message': 'No biography found'}, status=status.HTTP_404_NOT_FOUND)
