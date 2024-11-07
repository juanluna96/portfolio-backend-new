from apps.projects.models import ProjectDescription
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Delete all ProjectDescription data'

    def handle(self, *args, **options):
        # Confirmar la eliminación
        confirm = input("Are you sure you want to delete all ProjectDescription data? (yes/no): ")
        if confirm.lower() == 'yes':
            count, _ = ProjectDescription.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} ProjectDescription records'))
        else:
            self.stdout.write(self.style.WARNING('Operation cancelled'))
