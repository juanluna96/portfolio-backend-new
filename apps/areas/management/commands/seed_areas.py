from django.core.management.base import BaseCommand
from apps.areas.models import Area

class Command(BaseCommand):
    help = 'Seed data for the Area model'

    def handle(self, *args, **kwargs):
        areas = [
            {"title": "Frontend", "name": '{ "en": "Frontend Development", "es": "Desarrollo Frontend" }', "logo": "FaCss3Alt"},
            {"title": "Backend", "name": '{ "en": "Backend Development", "es": "Desarrollo Backend" }', "logo": "FaAws"},
            {"title": "Database", "name": '{ "en": "Database Management", "es": "Administracion BD" }', "logo": "FaDatabase"},
        ]

        for area_data in areas:
            Area.objects.create(**area_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded areas'))
