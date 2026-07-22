import os
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.companies.models import Company

class Command(BaseCommand):
    help = 'Seed data for the Company model with predefined companies'

    def handle(self, *args, **kwargs):
        companies = [
            {
                "name": "Datasistemas Web",
                "position": '{ "en": "Web Developer FullStack JR", "es": "Desarrollador Web FullStack JR" }',
                "image": "images/companies/DatasistemasWeb.png"
            },
            {
                "name": "Konecta",
                "position": '{ "en": "Development analyst", "es": "Analista de desarrollo" }',
                "image": "images/companies/Konecta.png"
            },
            {
                "name": "Habi",
                "position": '{ "en": "Web Developer MID", "es": "Desarrollador Web MID" }',
                "image": "images/companies/Habi.png"
            },
            {
                "name": "Personal",
                "position": '{ "en": "FullStack Dev", "es": "Desarrollador FullStack" }',
                "image": "images/companies/Personal.jpg"
            },
        ]

        for company_data in companies:
            # Comprobar si el archivo de imagen existe en la ruta esperada
            full_image_path = os.path.join(settings.MEDIA_ROOT, company_data["image"])
            if os.path.exists(full_image_path):
                _, created = Company.objects.get_or_create(
                    name=company_data["name"],
                    defaults={"position": company_data["position"], "image": company_data["image"]},
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Company "{company_data["name"]}" created.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Company "{company_data["name"]}" already exists, skipped.'))
            else:
                self.stdout.write(self.style.ERROR(f'Image file "{full_image_path}" not found'))

        self.stdout.write(self.style.SUCCESS('Seeding completed'))
