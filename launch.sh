#!/bin/bash

echo $'\n--- python manage.py makemigrations facturasieli ---'
.venv/bin/python3 Django\ project/manage.py makemigrations facturasieli

echo $'\n--- python manage.py migrate ---'
.venv/bin/python3 Django\ project/manage.py migrate

# echo $'\n--- python manage.py init_data ---'
# .venv/bin/python3 Django\ project/manage.py init_data

echo $'\n--- django-admin compilemessages ---'
.venv/bin/django-admin compilemessages --ignore .venv

echo $'\n--- docker compose up --build ---'
docker compose up --build
