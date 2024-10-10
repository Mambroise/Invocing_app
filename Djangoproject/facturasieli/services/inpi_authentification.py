# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/company_api.py
# Author : Morice
# ---------------------------------------------------------------------------

import requests
import environ
from django.conf import settings

# initialise environment
env = environ.Env()
environ.Env.read_env(env_file='.env')

class INPIAuthClient:
    BASE_URL = env('INPI_BASE_URL')
    AUTH_URL = env('INPI_AUTH_URL')

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None

    def authenticate(self):
        url = f"{self.BASE_URL}{self.AUTH_URL}"
        payload = {
            "username": self.username,
            "password": self.password,
        }
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Vérifie si la requête a échoué
            data = response.json()
            self.token = data.get('token')  # Récupère le token d'authentification

            if self.token:
                return self.token
            else:
                raise Exception("Authentification Fialaed: No token in response.")
            
        except requests.RequestException as e:
            raise Exception(f"authentification error: {e}")
        


