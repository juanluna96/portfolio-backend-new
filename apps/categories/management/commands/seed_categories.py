import os
import json
from django.core.management.base import BaseCommand
from apps.areas.models import Area
from apps.categories.models import Category
from main import settings

class Command(BaseCommand):
    help = 'Seed data for the Category model from a JSON file'

    def handle(self, *args, **kwargs):
        # Cargar el archivo JSON
        json_path = os.path.join(settings.BASE_DIR, 'apps', 'categories', 'management', 'commands', 'jsons', 'categories.json')
        with open(json_path, 'r', encoding='utf-8') as json_file:
            categories_data = json.load(json_file)

        for category_data in categories_data:
            # Obtener el área por título
            area_title = category_data["area"]
            area_instance = Area.objects.filter(title=area_title).first()

            if area_instance:
                Category.objects.create(
                    name=category_data["name"],
                    color_text=category_data["color_text"],
                    color_bg=category_data["color_bg"],
                    logo=category_data["logo"],
                    area_id=area_instance,
                    image=os.path.join("images/categories/", category_data["image"]),
                    imageBig=os.path.join("images/categories/", category_data["imageBig"])
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded categories from JSON'))
