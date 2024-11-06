from django.core.management.base import BaseCommand
from apps.categories.models import Category

class Command(BaseCommand):
    help = 'Delete seeded data for the Category model'

    def handle(self, *args, **kwargs):
        category_names = [
            "JavaScript", "React", "Angular", "Next.js",  # Frontend
            "Python", "PHP", "Django", "CodeIgniter", "Laravel", "Node.js",  # Backend
            "MongoDB", "MySQL", "PostgreSQL"  # Databases
        ]

        deleted_count, _ = Category.objects.filter(name__in=category_names).delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} seeded category records'))
