#!/bin/bash

# Ejecuta las eliminaciones de los seeds de la base de datos
echo "Eliminando fixtures..."


python manage.py delete_areas
echo "Áreas cargadas con éxito."

python manage.py delete_categories
echo "Categorías cargadas con éxito."


python manage.py delete_companies
echo "Empresas cargadas con éxito."

python manage.py delete_images_projects
echo "Imágenes de proyectos cargadas con éxito."

python manage.py delete_projects
echo "Proyectos cargados con éxito."

echo "Todos los fixtures han sido eliminados con éxito."

