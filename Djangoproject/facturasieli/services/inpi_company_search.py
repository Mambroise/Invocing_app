# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/company_api.py
# Author : Morice
# ---------------------------------------------------------------------------

import requests

from .inpi_authentification import INPIAuthClient

class INPICompanySearch:
    SEARCH_URL = "/api/companies"  

    def __init__(self, token):
        self.token = token

    def search_by_siren(self, siren):
        url = f"{INPIAuthClient.BASE_URL}{self.SEARCH_URL}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        params = {"siren[]": siren}  # Requête avec filtre par numéro SIREN

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Vérifie si la requête a échoué
            return response.json()  # Retourne les données de l'entreprise

        except requests.RequestException as e:
            raise Exception(f"Erreur de recherche de société: {e}")
