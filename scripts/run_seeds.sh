#!/bin/bash

# Ejecuta los seeds de los fixtures si los tienes
echo "Cargando fixtures..."


python manage.py seed_areas
echo "Áreas cargadas con éxito."

python manage.py seed_categories
echo "Categorías cargadas con éxito."


python manage.py seed_companies
echo "Empresas cargadas con éxito."

python manage.py seed_images_projects
echo "Imágenes de proyectos cargadas con éxito."

python manage.py seed_projects
echo "Proyectos cargados con éxito."

echo "Todos los fixtures han sido cargados con éxito."

