# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/create_company_service/create_company.py
# Author : Morice
# ---------------------------------------------------------------------------

from facturasieli.services.create_company_service.legal_form_1000 import create_company_1000
from facturasieli.services.create_company_service.legal_form_5499 import create_company_5499

def create_company_from_api_data(data):

    company = None
    # Extraire les données nécessaires de l'objet API
    legal_form = data['formality']['content']['natureCreation']['formeJuridique']
    if legal_form == "1000": # personne physique
      company = create_company_1000(data)
    elif legal_form == "5499": # Autre societe civile
      company = create_company_5499(data)
    elif legal_form == "5720": # SARL
       pass
    elif legal_form == "5480": # SAS
       pass
    elif legal_form == "5710": # SA
       pass
    elif legal_form == "5760": # SCI
       pass
    elif legal_form == "5720": # SCP
       pass
    else:
       pass
    
    return company

