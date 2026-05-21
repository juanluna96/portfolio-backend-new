from django.core.management.base import BaseCommand
from apps.areas.models import Area

AREA_LOGO_UPDATES = {
    'Frontend': 'FaReact',
    'Backend': 'FaServer',
    'Database': 'FaDatabase',
}

class Command(BaseCommand):
    help = 'Update Area logos to better match each area'

    def handle(self, *args, **kwargs):
        for title, logo in AREA_LOGO_UPDATES.items():
            updated = Area.objects.filter(title=title).update(logo=logo)
            if updated:
                self.stdout.write(self.style.SUCCESS(f'"{title}" logo → {logo}'))
            else:
                self.stdout.write(self.style.WARNING(f'"{title}" not found, skipped'))

        self.stdout.write(self.style.SUCCESS('Done'))
