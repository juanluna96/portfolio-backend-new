import json
import os
from django.core.management.base import BaseCommand
from apps.categories.models import Category, CategoryDescription
from apps.languages.models import Language
from main import settings

class Command(BaseCommand):
    help = 'Seed database with CategoryDescription data from a JSON file'

    def handle(self, *args, **kwargs):
        # Ruta al archivo JSON
        json_file_path = os.path.join(settings.BASE_DIR, 'apps', 'categories', 'management', 'commands', 'jsons', 'categories.json')

        if not os.path.exists(json_file_path):
            self.stdout.write(self.style.ERROR(f'JSON file not found at {json_file_path}'))
            return

        # Leer datos desde el archivo JSON
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        for entry in data:
            category_name = entry.get('name')
            descriptions = entry.get('descriptions', {})

            category = Category.objects.filter(name=category_name).first()
            if not category:
                self.stdout.write(self.style.WARNING(f'Category {category_name} not found. Skipping.'))
                continue

            for lang_code, desc_list in descriptions.items():
                language = Language.objects.filter(abbreviation=lang_code).first()
                if not language:
                    self.stdout.write(self.style.WARNING(f'Language with code {lang_code} not found. Skipping descriptions in {lang_code}.'))
                    continue

                for desc in desc_list:
                    _, created = CategoryDescription.objects.get_or_create(
                        category=category,
                        language=language,
                        description=desc,
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Added description for {category.name} in {language.name}: {desc}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Description already exists for {category.name} in {language.name}, skipped.'))

        self.stdout.write(self.style.SUCCESS('Category descriptions seeded successfully!'))
