from django.core.management.base import BaseCommand
from apps.projects.models import Project

class Command(BaseCommand):
    help = 'Delete all projects from the database'

    def handle(self, *args, **options):
        # Contar la cantidad de proyectos existentes
        project_count = Project.objects.count()

        if project_count == 0:
            self.stdout.write(self.style.WARNING('No hay proyectos para eliminar.'))
            return

        # Confirmación antes de eliminar
        self.stdout.write(self.style.WARNING(f'Se eliminarán {project_count} proyectos.'))
        
        Project.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Todos los proyectos ({project_count}) han sido eliminados.'))
