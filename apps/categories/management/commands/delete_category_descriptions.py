from django.core.management.base import BaseCommand
from apps.categories.models import CategoryDescription

class Command(BaseCommand):
    help = 'Delete all CategoryDescription data'

    def handle(self, *args, **kwargs):
        # Elimina todas las descripciones de categorías
        deleted_count, _ = CategoryDescription.objects.all().delete()
        
        # Muestra cuántos registros fueron eliminados
        if deleted_count:
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} category descriptions'))
        else:
            self.stdout.write(self.style.WARNING('No category descriptions found to delete'))
