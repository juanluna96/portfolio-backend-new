from django.core.management.base import BaseCommand
from apps.images_projects.models import ImageProject


class Command(BaseCommand):
    help = 'Elimina las imágenes de ejemplo de la base de datos'

    def handle(self, *args, **kwargs):
        # Obtener todas las imágenes de ejemplo
        images = ImageProject.objects.all()

        # Eliminar todas las imágenes
        images.delete()

        self.stdout.write(self.style.SUCCESS('Todas las imágenes fueron eliminadas con éxito.'))
