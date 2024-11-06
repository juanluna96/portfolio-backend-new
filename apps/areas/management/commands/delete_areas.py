from django.core.management.base import BaseCommand
from apps.areas.models import Area

class Command(BaseCommand):
    help = 'Delete seeded data for the Area model'

    def handle(self, *args, **kwargs):
        area_titles = ["Frontend", "Backend", "Databases", "DevOps", "Testing", "Mobile"]

        deleted_count, _ = Area.objects.filter(title__in=area_titles).delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} seeded area records'))
