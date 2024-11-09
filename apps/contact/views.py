from rest_framework import viewsets, mixins

from apps.contact.schemas import ContactSchema
from .serializer import ContactSerializer
from .models import Contact

class ContactViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    schema = ContactSchema()

    def create(self, request, *args, **kwargs):
        # Obtén el valor del parámetro 'language' desde la query
        language = request.query_params.get('language', 'en')  # Default to 'en' if not provided

        # Llamamos al método 'create' de la clase base para crear el contacto
        response = super().create(request, *args, **kwargs)

        # Determinar el mensaje según el idioma
        if language == 'es':
            message = '¡Gracias por ponerte en contacto con nosotros!'
        else:
            message = 'Thank you for contacting us!'

        # Agregar el mensaje al response data
        response.data['message'] = message

        return response