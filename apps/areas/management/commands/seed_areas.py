from django.core.management.base import BaseCommand
from apps.areas.models import Area

class Command(BaseCommand):
    help = 'Seed data for the Area model'

    def handle(self, *args, **kwargs):
        areas = [
            {"title": "Frontend", "name": "Frontend Development", "logo": "fa-solid fa-code"},
            {"title": "Backend", "name": "Backend Development", "logo": "fa-solid fa-server"},
            {"title": "Database", "name": "Database Management", "logo": "fa-solid fa-database"},
        ]

        for area_data in areas:
            Area.objects.create(**area_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded areas'))
