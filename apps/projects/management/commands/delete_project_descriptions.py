from apps.projects.models import ProjectDescription
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Delete all ProjectDescription data'

    def handle(self, *args, **options):
        # Confirmar la eliminación
        count, _ = ProjectDescription.objects.all().delete()
        print(f'Deleted {count} ProjectDescription records')
