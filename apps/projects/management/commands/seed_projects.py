import json
import os
import random
from django.core.management.base import BaseCommand
from apps.companies.models import Company
from apps.categories.models import Category
from apps.languages.models import Language
from apps.images_projects.models import ImageProject
from apps.projects.models import Project
from main import settings

class Command(BaseCommand):
    help = 'Seed the Project table with data from JSON file'

    def handle(self, *args, **options):
        # Ruta al archivo JSON
        json_path =  os.path.join(settings.BASE_DIR, 'apps', 'projects', 'management', 'commands', 'jsons', 'projects.json')
        
        # Verificar si el archivo existe
        if not os.path.exists(json_path):
            self.stdout.write(self.style.ERROR(f'El archivo "{json_path}" no existe.'))
            return

        # Cargar datos desde el archivo JSON
        with open(json_path, 'r', encoding='utf-8') as file:
            projects_data = json.load(file)

        # Eliminar todos los proyectos existentes
        self.stdout.write(self.style.WARNING('Eliminando todos los proyectos existentes...'))
        Project.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Todos los proyectos han sido eliminados.'))

        for project_data in projects_data:
            # Buscar la compañía por nombre
            company = Company.objects.filter(name=project_data['company']).first()
            if not company:
                self.stdout.write(self.style.WARNING(f'La compañía "{project_data["company"]}" no se encontró.'))
                continue

            # Obtener los idiomas por su código (e.g., 'en', 'es')
            languages = Language.objects.filter(abbreviation__in=project_data['languages'])
            if not languages.exists():
                self.stdout.write(self.style.WARNING(f'No se encontraron los idiomas {project_data["languages"]}.'))
                continue

            # Obtener las categorías por su nombre
            categories = Category.objects.filter(name__in=project_data['categories'])
            if not categories.exists():
                self.stdout.write(self.style.WARNING(f'No se encontraron las categorías {project_data["categories"]}.'))
                continue

            # Obtener las imágenes por nombre de archivo
            images = ImageProject.objects.filter(name__in=[os.path.splitext(img)[0] for img in project_data['images']])
            if not images.exists():
                self.stdout.write(self.style.WARNING(f'No se encontraron las imágenes {project_data["images"]}.'))
                continue

            # Crear el proyecto
            project = Project.objects.create(
                title=project_data['title'],
                url=project_data['url'],
                description=project_data['description']['es'],  # O cambiar a 'en' según sea necesario
                company=company,
            )
            
            project.language.set(languages)  # Asignar idiomas al proyecto

            # Asignar categorías y imágenes al proyecto
            project.categories.set(categories)
            project.images.set(images)
            project.save()

            self.stdout.write(self.style.SUCCESS(f'Proyecto "{project.title}" creado con éxito.'))

        self.stdout.write(self.style.SUCCESS('Seeding de proyectos completado.'))
