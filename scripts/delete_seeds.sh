#!/bin/bash

# Ejecuta las eliminaciones de los seeds de la base de datos
echo "Eliminando fixtures..."


python manage.py delete_areas
echo "Áreas eliminadas con éxito."

python manage.py delete_languages
echo "Claves de idioma eliminadas con éxito."

python manage.py delete_categories
echo "Categorías eliminadas con éxito."

python manage.py delete_category_descriptions
echo "Descripciones de categorías eliminadas con éxito."

python manage.py delete_companies
echo "Empresas eliminadas con éxito."

python manage.py delete_images_projects
echo "Imágenes de proyectos eliminadas con éxito."

python manage.py delete_projects
echo "Proyectos eliminados con éxito."

echo "Todos los fixtures han sido eliminados con éxito."

