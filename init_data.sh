#!/bin/bash

.venv/bin/python 'Django project'/manage.py loaddata initial_data/Addresses.json
.venv/bin/python 'Django project'/manage.py loaddata initial_data/Companies.json
.venv/bin/python 'Django project'/manage.py loaddata initial_data/Roles.json
.venv/bin/python 'Django project'/manage.py loaddata initial_data/Users.json
.venv/bin/python 'Django project'/manage.py loaddata initial_data/Services.json
.venv/bin/python 'Django project'/manage.py loaddata initial_data/Invoices.json

.venv/bin/python 'Django project'/manage.py loaddata initial_data/Notifications.json
.venv/bin/python 'Django project'/manage.py loaddata initial_data/Verifications.json
