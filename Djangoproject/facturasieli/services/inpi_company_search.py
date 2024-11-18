# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/company_api.py
# Author : Morice
# ---------------------------------------------------------------------------

import requests
from .inpi_authentification import INPIAuthClient

class INPICompanySearch:

    def __init__(self, token):
        self.token = token

    def search_by_siren_or_name(self, search):
        search_url= ''
        # check siren validity (9numbers)
        if search.isdigit() and len(search) == 9:
            params = {"siren[]": search}
            search_url = "/api/companies" 
        else:
            params = {"name": search}
            search_url = "/api/companies?companiesNames"  


        """
        Effectue une recherche d'entreprise soit par SIREN, soit par nom.
        
        :param search: numéro SIREN ou nom de société
        :return: données JSON de l'API
        """
        url = f"{INPIAuthClient.BASE_URL}{search_url}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }


        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Lève une exception pour les erreurs HTTP
            return response.json()

        except requests.RequestException as e:
            raise Exception(f"Erreur de recherche de société: {e}, Détails: {response.text if response else 'Aucune réponse'}")
