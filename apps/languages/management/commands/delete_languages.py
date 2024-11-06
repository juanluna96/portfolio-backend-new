from django.core.management.base import BaseCommand
from apps.languages.models import Language  # Cambia 'languages' por el nombre de la app donde está Language

class Command(BaseCommand):
    help = 'Delete seeded data for the Language model'

    def handle(self, *args, **kwargs):
        language_names = ["Español", "Ingles"]

        deleted_count, _ = Language.objects.filter(name__in=language_names).delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} seeded language records'))
