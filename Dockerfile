# Base: Python 3.13 (versión ligera)
FROM python:3.13-slim

# Instala dependencias del sistema necesarias para mysqlclient
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends default-libmysqlclient-dev gcc && \
#     rm -rf /var/lib/apt/lists/*
# Instala dependencias necesarias para MariaDB
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     libmariadb-dev \
#     pkg-config \
#     gcc && \
#     mariadb-client && \
#     rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copia requisitos e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY . .
# COPY wait-for-db.sh /usr/local/bin/wait-for-db.sh
# RUN chmod +x /usr/local/bin/wait-for-db.sh

# Puerto de Django
EXPOSE 8000

# Comando de ejecución (ajusta según entorno: desarrollo/producción)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["sh", "-c", "echo 'Esperando a que MySQL esté listo...' && ./wait-for-it.sh db:3306 -t 30 && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]