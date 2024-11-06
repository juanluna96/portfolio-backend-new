from django.core.management.base import BaseCommand
from apps.companies.models import Company

class Command(BaseCommand):
    help = 'Delete seeded data for the Company model'

    def handle(self, *args, **kwargs):
        company_names = ["Datasistemas Web", "Konecta", "Habi"]

        deleted_count, _ = Company.objects.filter(name__in=company_names).delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} seeded company records'))
