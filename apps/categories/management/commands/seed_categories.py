import os
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.areas.models import Area
from apps.categories.models import Category  # Cambia 'categories' por el nombre de tu app si es diferente

class Command(BaseCommand):
    help = 'Seed data for the Category model with images'

    def handle(self, *args, **kwargs):
        # Obtener las áreas existentes
        frontend_area = Area.objects.get(title="Frontend")
        backend_area = Area.objects.get(title="Backend")
        database_area = Area.objects.get(title="Database")

        categories = [
            # Frontend
            {
                "name": "JavaScript",
                "color_text": "#FFFFFF",
                "color_bg": "#F7DF1E",
                "logo": "fa-brands fa-js",
                "area": frontend_area,
                "image": "frontend_js.png",
                "imageBig": "frontend_js_big.png"
            },
            {
                "name": "React",
                "color_text": "#FFFFFF",
                "color_bg": "#61DAFB",
                "logo": "fa-brands fa-react",
                "area": frontend_area,
                "image": "frontend_react.png",
                "imageBig": "frontend_react_big.png"
            },
            {
                "name": "Angular",
                "color_text": "#FFFFFF",
                "color_bg": "#DD0031",
                "logo": "fa-brands fa-angular",
                "area": frontend_area,
                "image": "frontend_angular.png",
                "imageBig": "frontend_angular_big.png"
            },
            {
                "name": "Next.js",
                "color_text": "#FFFFFF",
                "color_bg": "#000000",
                "logo": "fa-brands fa-nextjs",
                "area": frontend_area,
                "image": "frontend_nextjs.png",
                "imageBig": "frontend_nextjs_big.png"
            },
            # Backend
            {
                "name": "Python",
                "color_text": "#FFFFFF",
                "color_bg": "#3776AB",
                "logo": "fa-brands fa-python",
                "area": backend_area,
                "image": "backend_python.png",
                "imageBig": "backend_python_big.png"
            },
            {
                "name": "PHP",
                "color_text": "#FFFFFF",
                "color_bg": "#777BB4",
                "logo": "fa-brands fa-php",
                "area": backend_area,
                "image": "backend_php.png",
                "imageBig": "backend_php_big.png"
            },
            {
                "name": "Django",
                "color_text": "#FFFFFF",
                "color_bg": "#092E20",
                "logo": "fa-brands fa-django",
                "area": backend_area,
                "image": "backend_django.png",
                "imageBig": "backend_django_big.png"
            },
            {
                "name": "CodeIgniter",
                "color_text": "#FFFFFF",
                "color_bg": "#EF4223",
                "logo": "fa-brands fa-codeigniter",
                "area": backend_area,
                "image": "backend_codeigniter.png",
                "imageBig": "backend_codeigniter_big.png"
            },
            {
                "name": "Laravel",
                "color_text": "#FFFFFF",
                "color_bg": "#FF2D20",
                "logo": "fa-brands fa-laravel",
                "area": backend_area,
                "image": "backend_laravel.png",
                "imageBig": "backend_laravel_big.png"
            },
            {
                "name": "Node.js",
                "color_text": "#FFFFFF",
                "color_bg": "#339933",
                "logo": "fa-brands fa-node-js",
                "area": backend_area,
                "image": "backend_nodejs.png",
                "imageBig": "backend_nodejs_big.png"
            },
            # Database
            {
                "name": "MongoDB",
                "color_text": "#FFFFFF",
                "color_bg": "#47A248",
                "logo": "fa-brands fa-mongodb",
                "area": database_area,
                "image": "database_mongodb.png",
                "imageBig": "database_mongodb_big.png"
            },
            {
                "name": "MySQL",
                "color_text": "#FFFFFF",
                "color_bg": "#4479A1",
                "logo": "fa-brands fa-mysql",
                "area": database_area,
                "image": "database_mysql.png",
                "imageBig": "database_mysql_big.png"
            },
            {
                "name": "PostgreSQL",
                "color_text": "#FFFFFF",
                "color_bg": "#336791",
                "logo": "fa-brands fa-postgresql",
                "area": database_area,
                "image": "database_postgresql.png",
                "imageBig": "database_postgresql_big.png"
            },
        ]

        for category_data in categories:
            image_path = os.path.join("category_images", category_data["image"])
            imageBig_path = os.path.join("category_images", category_data["imageBig"])

            Category.objects.create(
                name=category_data["name"],
                color_text=category_data["color_text"],
                color_bg=category_data["color_bg"],
                logo=category_data["logo"],
                area_id=category_data["area"],
                image=image_path,
                imageBig=imageBig_path
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded categories with images'))
