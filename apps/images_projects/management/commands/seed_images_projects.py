from django.core.management.base import BaseCommand
from apps.images_projects.models import ImageProject
from django.core.files import File
from io import BytesIO
from PIL import Image as PILImage
import random


class Command(BaseCommand):
    help = 'Crea imágenes de ejemplo para asociarlas a los proyectos'

    def generate_image(self, name):
        """
        Genera una imagen en memoria y la devuelve como un archivo.
        """
        # Crear una imagen simple con PIL
        image = PILImage.new('RGB', (100, 100), color='blue')  # Imagen de 100x100 píxeles de color azul
        image_file = BytesIO()
        image.save(image_file, format='PNG')
        image_file.seek(0)

        # Crear el archivo en Django
        image_instance = ImageProject(name=name)
        image_instance.image.save(f"{name}.png", File(image_file), save=False)
        return image_instance

    def handle(self, *args, **kwargs):
        # Crear 10 imágenes de ejemplo
        for i in range(10):
            name = f"Imagen_{i+1}"

            # Generar la imagen
            image_instance = self.generate_image(name)

            # Guardar la instancia de imagen
            image_instance.save()

            self.stdout.write(self.style.SUCCESS(f'Imagen "{name}" creada con éxito.'))
