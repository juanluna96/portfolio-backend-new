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
                file_path = os.path.join(directory, filename)

                # Extraer el nombre del archivo sin la extensión
                name = os.path.splitext(filename)[0]

                image_instance = ImageProject(name=name, image=f'images/projects/{filename}')
                image_instance.save()

                self.stdout.write(self.style.SUCCESS(f'Imagen "{name}" procesada y almacenada.'))