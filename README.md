# Proyecto Backend - Portfolio

Este es el backend para el proyecto de **Portfolio**. El backend está desarrollado con **Django** y usa **Docker** para su despliegue y configuración. Además, se integra con una base de datos **PostgreSQL**.

## Estructura del Proyecto

```plaintext
├── apps/                   # Aplicaciones de Django
│   ├── areas/              # Gestión de áreas de programación
│   ├── categories/         # Categorías de los proyectos
│   ├── companies/          # Información sobre empresas
│   └── ...
├── main/                   # Configuración principal del proyecto
│   ├── settings.py         # Configuración global de Django
│   └── ...
├── management/             # Comandos personalizados de Django
│   └── ...
├── scripts/                # Scripts de utilidades (como migraciones y seeds)
│   ├── wait-for-db.sh      # Script para esperar que la base de datos esté disponible
│   ├── migrate_db.sh       # Script para ejecutar migraciones
│   └── run_seeds.sh        # Script para insertar datos iniciales (seeds)
├── Dockerfile              # Archivo de configuración para Docker
├── docker-compose.yml      # Configuración de los contenedores Docker
└── .env                    # Variables de entorno (base de datos, superusuario, etc.)
```

Requisitos
----------

Para ejecutar este proyecto, necesitarás tener instalados los siguientes programas:

### 1\. **Docker**

Docker es necesario para crear contenedores de los servicios de la aplicación, como la base de datos y el backend de Django. Puedes descargar Docker desde su sitio oficial.

### 2\. **Docker Compose**

Docker Compose es una herramienta que permite definir y ejecutar aplicaciones de varios contenedores. Con Docker Compose, podrás configurar fácilmente la infraestructura necesaria para tu proyecto. Puedes descargar Docker Compose desde su sitio oficial.

### 3\. **Django**

Este proyecto está construido sobre Django, un framework de Python para el desarrollo web. Aunque Docker manejará la instalación de Django dentro del contenedor, es útil tenerlo instalado localmente para ejecutar comandos como tests o migraciones manualmente.

### 4\. **PostgreSQL**

El proyecto usa PostgreSQL como base de datos. Docker se encargará de la instalación y configuración de PostgreSQL dentro de un contenedor, por lo que no necesitas instalar PostgreSQL de forma local.

Configuración
-------------

### 1\. **Clonación del repositorio**

Clona el repositorio del proyecto en tu máquina local:

```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
```

### 2\. **Configuración del archivo `.env`**

Dentro del directorio raíz de tu proyecto, crea un archivo `.env` con las siguientes variables de entorno. Este archivo contiene información crucial como las credenciales de la base de datos y la configuración del superusuario para Django.

```
    DB_NAME=portfolio_db
    DB_USER=postgres
    DB_PASSWORD=root
    DB_HOST=localhost
    DB_PORT=5433

    DJANGO_SUPERUSER_USERNAME=admin
    DJANGO_SUPERUSER_PASSWORD=admin
    DJANGO_SUPERUSER_EMAIL=admin@example.com
```

-   **DB_NAME**: El nombre de la base de datos (en este caso `portfolio_db`).
-   **DB_USER**: El nombre de usuario para acceder a la base de datos (por ejemplo, `postgres`).
-   **DB_PASSWORD**: La contraseña del usuario de la base de datos (en este caso, `root`).
-   **DB_HOST**: El host donde se encuentra la base de datos (por defecto, se usará `localhost`).
-   **DB_PORT**: El puerto de conexión a la base de datos (en este caso, `5433`).
-   **DJANGO_SUPERUSER_USERNAME**: El nombre de usuario para el superusuario de Django.
-   **DJANGO_SUPERUSER_PASSWORD**: La contraseña del superusuario de Django.
-   **DJANGO_SUPERUSER_EMAIL**: El correo electrónico del superusuario de Django.

### 3\. **Construcción y ejecución de los contenedores Docker**

Una vez que hayas configurado el archivo `.env`, puedes proceder a construir y ejecutar los contenedores necesarios para el proyecto con el siguiente comando:

```bash
    docker-compose up --build
```

Este comando construirá los contenedores (si es la primera vez que los ejecutas) y pondrá en marcha los servicios definidos en el archivo `docker-compose.yml` (como la base de datos y el backend de Django).

### 4\. **Esperar que la base de datos esté lista**

El contenedor de Django contiene un script `migrate_db.sh` que garantiza que la base de datos esté completamente lista antes de intentar ejecutar las migraciones o iniciar el servidor. Este script espera a que la base de datos esté disponible para realizar las operaciones necesarias.

### 5\. **Ejecutar migraciones y seeds**

Al iniciar los contenedores, se ejecutarán automáticamente las migraciones de Django y los seeds definidos. Si deseas ejecutar las migraciones manualmente, puedes hacerlo con el siguiente comando:

```bash
    docker-compose exec web python manage.py migrate
```

Si deseas ejecutar los seeds de la base de datos manualmente, usa el siguiente comando:

```bash
    docker-compose exec web /scripts/run_seeds.sh
```

Comandos de Django
------------------

Dentro del contenedor de Django, puedes ejecutar los siguientes comandos:

1.  **Migrar la base de datos**:

```bash 
    docker-compose exec web python manage.py migrate
```

2.  **Crear un superusuario (si no se ha creado automáticamente)**:

```bash 
    docker-compose exec web python manage.py createsuperuser
```

3.  **Ejecutar tests**:

```bash
    docker-compose exec web python manage.py test
```

Docker Compose
--------------

### Servicios

El archivo `docker-compose.yml` define dos servicios principales:

1.  **web**: El contenedor que ejecuta la aplicación Django.
2.  **db**: El contenedor que ejecuta PostgreSQL como base de datos.

### Comandos útiles

-   **Levantar los servicios**:

```bash
    docker-compose up
```

-   **Detener los servicios**:

```bash
    docker-compose down
```    

-   **Reiniciar los contenedores**:

```bash
    docker-compose restart
```

Contribución
------------

Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:

1.  Haz un fork del repositorio.
2.  Crea una rama nueva (`git checkout -b feature/nueva-caracteristica`).
3.  Realiza tus cambios y haz un commit (`git commit -am 'Añadir nueva característica'`).
4.  Envía un pull request.

Licencia
--------

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
