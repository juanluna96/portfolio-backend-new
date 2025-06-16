#!/bin/bash

# Cargar variables de entorno desde .env
if [ -f .env ]; then
    echo "Cargando variables de entorno desde .env"
    export $(grep -v '^#' .env | xargs)
else
    echo "Error: No se encontró el archivo .env"
    exit 1
fi

# Actualizar Zappa con las variables de entorno
echo "Actualizando Zappa..."
zappa update dev

# Verificar si el comando anterior fue exitoso
if [ $? -eq 0 ]; then
    echo "\nZappa actualizado exitosamente!"
    echo "\nEjecutando migraciones..."
    zappa manage dev migrate
    
    echo "\nProceso completado!"
else
    echo "\nError al actualizar Zappa. Revisa los mensajes de error."
    exit 1
fi
