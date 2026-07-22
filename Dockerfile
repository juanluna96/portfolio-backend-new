# Dockerfile

# Usa una imagen base para Django
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /code

# Instala dependencias de sistema necesarias (netcat-openbsd, etc.)
RUN apt-get update && apt-get install -y netcat-openbsd

# Copia el archivo requirements.txt (y otros archivos si es necesario)
COPY requirements.txt /code/

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Copia el código de tu aplicación y el directorio scripts
COPY . /code/
COPY ./scripts /scripts

# Da permisos de ejecución al script
RUN chmod +x /scripts/run_seeds.sh
RUN chmod +x /code/scripts/migrate_db.sh

# Comando para ejecutar el contenedor (el contenedor usará migrate_db.sh)
CMD ["/bin/sh", "/code/scripts/migrate_db.sh"]
