from django.core.management.base import BaseCommand
from apps.categories.models import Category, CategoryDescription
from apps.languages.models import Language

class Command(BaseCommand):
    help = 'Seed database with CategoryDescription data'

    def handle(self, *args, **kwargs):
        # Verifica que haya al menos una categoría y un idioma en la base de datos
        if not Category.objects.exists():
            self.stdout.write(self.style.ERROR('No categories found. Please add categories first.'))
            return

        if not Language.objects.exists():
            self.stdout.write(self.style.ERROR('No languages found. Please add languages first.'))
            return

        # Crear datos de ejemplo
        categories = Category.objects.all()
        languages = Language.objects.all()

        for category in categories:
            for language in languages:
                # Verifica si ya existe una descripción para evitar duplicados
                if not CategoryDescription.objects.filter(category=category, language=language).exists():
                    CategoryDescription.objects.create(
                        category=category,
                        language=language,
                        description=f'Description of {category.name} in {language.name}'
                    )
                    self.stdout.write(self.style.SUCCESS(f'Successfully added description for {category.name} in {language.name}'))

        self.stdout.write(self.style.SUCCESS('Category descriptions seeded successfully!'))
