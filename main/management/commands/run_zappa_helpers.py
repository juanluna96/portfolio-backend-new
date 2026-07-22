from django.core.management.base import BaseCommand
import importlib

class Command(BaseCommand):
    help = 'Run commands from zappa_helpers.py'

    def handle(self, *args, **options):
        # Importar y ejecutar cada función de zappa_helpers
        helpers = importlib.import_module('zappa_helpers')
        
        # Crear superusuario
        self.stdout.write(self.style.SUCCESS('Creating superuser...'))
        helpers.create_superuser()
        
        # Ejecutar todos los seeds
        self.stdout.write(self.style.SUCCESS('Running all seeds...'))
        helpers.run_all_seeds()
