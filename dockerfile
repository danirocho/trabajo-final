FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

# WORKDIR dentro del contenedor
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

