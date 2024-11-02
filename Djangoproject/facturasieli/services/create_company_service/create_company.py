# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/create_company_service/create_company.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.contrib import messages
from facturasieli.services.create_company_service.legal_form_1000 import create_company_1000
from facturasieli.services.create_company_service.legal_form_5499 import create_company_5499
from facturasieli.services.create_company_service.legal_form_5710 import create_company_5710

def create_company_from_api_data(request,data):

   # list of code eligible with the app
    entrepreneurs = [
   "1000",  # Entreprise individuelle générale
   "1100",  # Entreprise individuelle artisanale
   "1200",  # Entreprise individuelle commerciale
   "1300",  # Entreprise individuelle libérale
   "1400",  # Entreprise individuelle agricole
   "1500",  # Micro-entreprise (auto-entrepreneur)
   "1510",  # Auto-entrepreneur commerçant
   "1520",  # Auto-entrepreneur artisan
   "1530"   # Auto-entrepreneur libéral
    ]

    sarl_code = ['5720','6550','6530','5480','6540']

    company = None
    # Extraire les données nécessaires de l'objet API
    legal_form = data['formality']['content']['natureCreation']['formeJuridique']
    if legal_form == "1000": # personne physique
      company = create_company_1000(data)
    elif legal_form == "5499": # Autre societe civile
      company = create_company_5499(data)
    elif legal_form in sarl_code: # SARL
       messages.warning(request,_('The companies with this legal structure are not compatible with the application at the moment.'))
    elif legal_form == "5480": # SAS
       messages.warning(request,_('The companies with this legal structure are not compatible with the application at the moment.'))    
    elif legal_form == "5710": # SA
       messages.warning(request,_('The companies with this legal structure are not compatible with the application at the moment.'))    
       #company = create_company_5710(data)
    elif legal_form == "5760": # SCI
       pass
    elif legal_form == "5720": # SCP
       pass
    else:
       pass
    
    return company

