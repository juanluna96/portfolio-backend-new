# scripts/seed_project_descriptions.py
from apps.projects.models import Project, ProjectDescription
from apps.languages.models import Language
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Seed the database with ProjectDescription data'

    def handle(self, *args, **options):
        # Ejemplo de datos para los seeds
        projects = Project.objects.all()
        languages = Language.objects.all()

        for project in projects:
            for language in languages:
                # Verificar si ya existe la descripción para este proyecto y lenguaje
                if not ProjectDescription.objects.filter(project=project, language=language).exists():
                    ProjectDescription.objects.create(
                        project=project,
                        language=language,
                        description=f'Descripción de ejemplo para {project.title} en {language.name}'
                    )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded ProjectDescription data'))
