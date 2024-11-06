from rest_framework import viewsets, mixins
from .serializer import ContactSerializer
from .models import Contact

class ContactViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer