from django.core.management.base import BaseCommand
from apps.areas.models import Area

class Command(BaseCommand):
    help = 'Seed data for the Area model'

    def handle(self, *args, **kwargs):
        areas = [
            {"title": "Frontend",    "name": '{ "en": "Frontend Development",      "es": "Desarrollo Frontend" }',        "logo": "FaReact",   "ad_id": "Ad001"},
            {"title": "Backend",     "name": '{ "en": "Backend Development",       "es": "Desarrollo Backend" }',         "logo": "FaServer",  "ad_id": "Ad002"},
            {"title": "Database",    "name": '{ "en": "Database Management",       "es": "Administracion BD" }',          "logo": "FaDatabase","ad_id": "Ad003"},
            {"title": "Video Games", "name": '{ "en": "Video Game Development",    "es": "Desarrollo de Videojuegos" }',  "logo": "FaGamepad", "ad_id": "Ad004"},
            {"title": "AI",          "name": '{ "en": "Artificial Intelligence",   "es": "Inteligencia Artificial" }',    "logo": "FaBrain",   "ad_id": "Ad005"},
        ]

        for area_data in areas:
            _, created = Area.objects.update_or_create(
                title=area_data['title'],
                defaults={k: v for k, v in area_data.items() if k != 'title'},
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Area "{area_data["title"]}" created.'))
            else:
                self.stdout.write(self.style.WARNING(f'Area "{area_data["title"]}" updated.'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded areas'))
