from django.core.management.base import BaseCommand
from apps.languages.models import Language  # Cambia 'your_app' al nombre real de tu app

class Command(BaseCommand):
    help = 'Seed data for the Language model'

    def handle(self, *args, **kwargs):
        languages = [
            {"name": "Español", "description": "spanish", "abbreviation": "es", "flag": "ES"},
            {"name": "Inglés", "description": "english", "abbreviation": "en", "flag": "US"},
        ]

        for lang_data in languages:
            _, created = Language.objects.get_or_create(abbreviation=lang_data['abbreviation'], defaults=lang_data)
            if not created:
                self.stdout.write(self.style.WARNING(f'Language "{lang_data["abbreviation"]}" already exists, skipped.'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded languages'))
