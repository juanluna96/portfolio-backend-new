from django.core.management.base import BaseCommand
from apps.information.models import Biography

class Command(BaseCommand):
    help = 'Deletes all Biography data from the database'

    def handle(self, *args, **kwargs):
        count, _ = Biography.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} Biography entries'))
