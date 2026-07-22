import json
import os
from django.core.management.base import BaseCommand
from apps.projects.models import Project, ProjectDescription
from apps.languages.models import Language
from main import settings

class Command(BaseCommand):
    help = 'Seed the database with ProjectDescription data from jsons/projects.json'

    def handle(self, *args, **options):
        json_path =  os.path.join(settings.BASE_DIR, 'apps', 'projects', 'management', 'commands', 'jsons', 'projects.json')
        
        # Verificar si el archivo existe
        if not os.path.exists(json_path):
            self.stdout.write(self.style.ERROR(f'El archivo "{json_path}" no existe.'))
            return

        # Cargar datos desde el archivo JSON
        with open(json_path, 'r', encoding='utf-8') as file:
            project_data = json.load(file)
        
        for project_entry in project_data:
            project_title = project_entry['title']
            project = Project.objects.filter(title=project_title).first()
            
            if not project:
                self.stdout.write(self.style.WARNING(f'Project "{project_title}" not found in the database. Skipping.'))
                continue
            
            descriptions = project_entry.get('description', {})
            
            for lang_code, description_text in descriptions.items():
                language = Language.objects.filter(abbreviation=lang_code).first()
                
                if not language:
                    self.stdout.write(self.style.WARNING(f'Language "{lang_code}" not found in the database. Skipping.'))
                    continue
                
                # Verificar si ya existe la descripción para este proyecto y lenguaje
                if not ProjectDescription.objects.filter(project=project, language=language).exists():
                    ProjectDescription.objects.create(
                        project=project,
                        language=language,
                        description=description_text
                    )
                    self.stdout.write(self.style.SUCCESS(f'Successfully added description for "{project_title}" in "{language.name}".'))
                else:
                    self.stdout.write(f'Description for "{project_title}" in "{language.name}" already exists. Skipping.')
        
        self.stdout.write(self.style.SUCCESS('Seeding of ProjectDescription data completed successfully'))
