FROM debian:bookworm

RUN apt update
RUN apt install -y gettext
RUN apt install -y python3-venv

# Échappez les espaces en les entourant de guillemets
WORKDIR /"Djangoproject"

RUN python3 -m venv .venv
RUN .venv/bin/python3 -m pip install --upgrade pip

COPY requirements.txt .
RUN .venv/bin/python3 -m pip install -r requirements.txt

COPY . .

CMD .venv/bin/python3 manage.py runserver 0.0.0.0:8000
