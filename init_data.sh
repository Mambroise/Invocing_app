#!/bin/bash

.venv/Scripts/python 'Django project'/manage.py loaddata initial_data/Addresses.json
.venv/Scripts/python 'Django project'/manage.py loaddata initial_data/Companies.json
.venv/Scripts/python 'Django project'/manage.py loaddata initial_data/Roles.json
.venv/Scripts/python 'Django project'/manage.py loaddata initial_data/Users.json
.venv/Scripts/python 'Django project'/manage.py loaddata initial_data/Services.json
.venv/Scripts/python 'Django project'/manage.py loaddata initial_data/Invoices.json

.venv/Scripts/python 'Django project'/manage.py loaddata initial_data/Notifications.json
.venv/Scripts/python 'Django project'/manage.py loaddata initial_data/Verifications.json
