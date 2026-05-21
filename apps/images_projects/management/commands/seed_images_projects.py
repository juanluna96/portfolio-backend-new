from django.core.management.base import BaseCommand
from apps.images_projects.models import ImageProject
from django.core.files import File
import os

from main import settings

class Command(BaseCommand):
    help = 'Lee todas las imágenes PNG en /media/images/projects y las almacena en la base de datos'

    def handle(self, *args, **kwargs):
        directory = os.path.join(settings.MEDIA_ROOT, 'images/projects')
        if not os.path.exists(directory):
            self.stdout.write(self.style.ERROR(f'El directorio "{directory}" no existe.'))
            return

        # Iterar sobre todos los archivos en el directorio
        for filename in os.listdir(directory):
            if filename.endswith('.png'):
                name = os.path.splitext(filename)[0]

                _, created = ImageProject.objects.get_or_create(
                    name=name,
                    defaults={'image': f'images/projects/{filename}'},
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Imagen "{name}" creada.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Imagen "{name}" ya existe, omitida.'))