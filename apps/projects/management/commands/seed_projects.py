import random
from django.core.management.base import BaseCommand
from apps.companies.models import Company
from apps.categories.models import Category
from apps.languages.models import Language
from apps.images_projects.models import ImageProject
from apps.projects.models import Project

class Command(BaseCommand):
    help = 'Seed the Project table with sample data'

    def handle(self, *args, **options):
        # Eliminar todos los proyectos existentes
        self.stdout.write(self.style.WARNING('Eliminando todos los proyectos existentes...'))
        Project.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Todos los proyectos han sido eliminados.'))

        # Obtener instancias existentes de otros modelos
        companies = Company.objects.all()
        categories = Category.objects.all()
        languages = Language.objects.all()
        images = ImageProject.objects.all()

        if not (companies.exists() and categories.exists() and languages.exists() and images.exists()):
            self.stdout.write(self.style.ERROR('Es necesario tener al menos una instancia de Company, Category, Language e ImageProject.'))
            return

        # Crear datos de ejemplo para proyectos
        for i in range(5):  # Crea 5 proyectos de ejemplo
            project = Project.objects.create(
                title=f'Project {i + 1}',
                url=f'https://www.example.com/project-{i + 1}',
                description=f'This is a description for Project {i + 1}.',
                company=random.choice(companies),
                language=random.choice(languages),
            )

            # Asignar categorías y imágenes de forma aleatoria
            project.categories.set(random.sample(list(categories), k=2))  # Asigna 2 categorías al azar
            project.images.set(random.sample(list(images), k=3))  # Asigna 3 imágenes al azar

            project.save()
            self.stdout.write(self.style.SUCCESS(f'Proyecto {project.title} creado.'))

        self.stdout.write(self.style.SUCCESS('Seeding de proyectos completado.'))
