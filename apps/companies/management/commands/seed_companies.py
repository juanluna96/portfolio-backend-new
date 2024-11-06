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
                "position": "Web Developer FullStack JR",
                "image": "datasistemas_web.png"
            },
            {
                "name": "Konecta",
                "position": "Analista de desarrollo",
                "image": "konecta.png"
            },
            {
                "name": "Habi",
                "position": "Web Developer MID",
                "image": "habi.png"
            },
        ]

        for company_data in companies:
            # Construir la ruta de la imagen a partir de MEDIA_ROOT
            image_path = os.path.join(settings.MEDIA_ROOT, "company_images", company_data["image"])

            Company.objects.create(
                name=company_data["name"],
                position=company_data["position"],
                image=image_path
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded company data'))
