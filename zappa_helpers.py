# zappa_helpers.py

import os
import django
from django.contrib.auth import get_user_model
from django.core import management

# Setup Django (esto es importante fuera de manage.py)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

admin_user = os.getenv("DJANGO_SUPERUSER_USERNAME")
admin_email = os.getenv("DJANGO_SUPERUSER_EMAIL")
admin_password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

def create_superuser():
    User = get_user_model()

    if not User.objects.filter(username=admin_user).exists():
        User.objects.create_superuser(admin_user, admin_email, admin_password)
        print("✅ Superuser created successfully")
    else:
        print("⚠️ Superuser already exists")

def delete_superuser():
    User = get_user_model()

    try:
        user = User.objects.get(username=admin_user)
        user.delete()
        print("🗑️ Superuser deleted successfully")
    except User.DoesNotExist:
        print("⚠️ Superuser does not exist")
        
def run_all_seeds():
    commands = [
        ("seed_areas", "Áreas"),
        ("seed_languages", "Idiomas"),
        ("seed_categories", "Categorías"),
        ("seed_category_descriptions", "Descripciones de categorías"),
        ("seed_companies", "Empresas"),
        ("seed_biography", "Biografías"),
        ("seed_images_projects", "Imágenes de proyectos"),
        ("seed_projects", "Proyectos"),
        ("seed_project_descriptions", "Descripciones de proyectos"),
    ]

    for cmd, label in commands:
        try:
            print(f"📦 Ejecutando: {cmd}")
            management.call_command(cmd)
            print(f"✅ {label} cargadas con éxito.\n")
        except Exception as e:
            print(f"❌ Error ejecutando {cmd}: {e}")

def delete_all_seeds():
    commands = [
        ("delete_areas", "Áreas"),
        ("delete_languages", "Idiomas"),
        ("delete_categories", "Categorías"),
        ("delete_category_descriptions", "Descripciones de categorías"),
        ("delete_companies", "Empresas"),
        ("delete_biography", "Biografías"),
        ("delete_images_projects", "Imágenes de proyectos"),
        ("delete_projects", "Proyectos"),
        ("delete_project_descriptions", "Descripciones de proyectos"),
    ]

    for cmd, label in commands:
        try:
            print(f"🧹 Ejecutando: {cmd}")
            management.call_command(cmd)
            print(f"✅ {label} eliminadas con éxito.\n")
        except Exception as e:
            print(f"❌ Error ejecutando {cmd}: {e}")