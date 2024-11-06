from django.core.management.base import BaseCommand
from apps.languages.models import Language  # Cambia 'your_app' al nombre real de tu app

class Command(BaseCommand):
    help = 'Seed data for the Language model'

    def handle(self, *args, **kwargs):
        languages = [
            {"name": "Español", "description": "spanish", "abbreviation": "es", "flag": "es"},
            {"name": "Inglés", "description": "english", "abbreviation": "en", "flag": "gb"},
        ]

        for lang_data in languages:
            Language.objects.create(**lang_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded languages'))
