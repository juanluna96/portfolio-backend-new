#!/bin/bash
# wait-for-db.sh
# Este script espera hasta que la base de datos esté disponible

# Esperar hasta que la base de datos esté disponible
while ! nc -z db 5432; do
  echo "Esperando a que la base de datos esté lista..."
  sleep 1
done

echo "Base de datos lista. Ejecutando migraciones..."

# Ejecutar migraciones de Django
python manage.py makemigrations
python manage.py migrate

# Ahora ejecuta los seeds
/scripts/run_seeds.sh

# Crear superusuario si no existe
python manage.py shell -c "
from django.contrib.auth import get_user_model;
from django.core.exceptions import ObjectDoesNotExist;
User = get_user_model();
try:
    User.objects.get(username='${DJANGO_SUPERUSER_USERNAME}');
    print('El superusuario ya existe.');
except ObjectDoesNotExist:
    User.objects.create_superuser(
        username='${DJANGO_SUPERUSER_USERNAME}', 
        email='${DJANGO_SUPERUSER_EMAIL}', 
        password='${DJANGO_SUPERUSER_PASSWORD}'
    );
    print('Superusuario creado.');
"

# Iniciar el servidor de Django
python manage.py runserver 0.0.0.0:8000
