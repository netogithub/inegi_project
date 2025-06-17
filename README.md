# 🌐 Proyecto INEGI API

## 📌 Descripción
Este proyecto consume datos del API INEGI y los organiza en una API REST con Django y Docker.

## 🧱 Tecnologías usadas
- Django
- Django REST Framework
- MySQL
- Docker + Docker Compose
- drf-spectacular (documentación)

## 📦 Requisitos
- Python 3.13
- Docker y Docker Compose
- MySQL Client

## 📥 Instalación
1. Clona el repositorio:
    ```bash
   git clone https://github.com/netogithub/inegi_project 
   cd inegi-api
   ```

2. Crea archivo .env:
    ```bash
    ```

3. Edita .env con tus variables:
    ```bash
    # .env.example
    DEBUG=True
    SECRET_KEY=tu_clave_secreta_aqui

    # Configuración de la base de datos
    DB_ENGINE=django.db.backends.mysql
    DB_NAME=mydatabase
    DB_USER=myuser
    DB_PASSWORD=mypassword
    DB_HOST=db
    DB_PORT=3306
    ```

4. Construye los contenedores:
    ```bash
    docker-compose build
    docker-compose up
    ```

5. Carga datos del INEGI:
    ```bash
    docker exec -it web python manage.py populate_inegi
    ```

## 📊 Endpoints disponibles

-Estados
    ```bash
    GET /api/estados/ - Lista todos los estados
    GET /api/estados/?estado=01/ - Detalle de un estado
    -Municipios
    GET /api/municipios/?estado=01 - Municipios del estado 01
    GET /api/municipios/?estado=01&municipio=001 - Detalle de un municipio
    -Localidades
    GET /api/localidades/?estado=01&municipio=001 - Localidades del municipio 001 del estado 01
    GET /api/localidades/?estado=01&municipio=001&localidad=0001 - Detalle de una localidad
    -Asentamientos
    GET /api/asentamientos/?estado=01&municipio=001&localidad=0001 - Asentamientos de la localidad 0001 del municipio 001 del estado 01
    GET /api/asentamientos/?estado=01&municipio=001&localidad=0001&asentamientos=0001 - Detalle de un asentamiento
    ```

## 📈 Documentación de la API

Accede a:

Swagger : http://localhost:8000/api/swagger/