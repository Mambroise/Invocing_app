# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/create_company_service/create_company.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from facturasieli.services.create_company_service.legal_form_1000 import create_company_1000
from facturasieli.services.create_company_service.legal_form_5499 import create_company_5499
from facturasieli.services.create_company_service.legal_form_5710 import create_company_5710

def create_company_from_api_data(request,data):

    company = []
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
    print(data)
    for data_object in data:
      # Extraire les données nécessaires de l'objet API
      legal_form = data_object['formality']['content']['natureCreation']['formeJuridique']
      if legal_form in entrepreneurs: # personne physique
         print('Entrepreneur 1111100000000')
         print(data_object)
         company_1000 = create_company_1000(data_object)
         company.append(company_1000)
      elif legal_form == "5499": # Autre societe civile
         print(data_object)
         print('Dans la 5499')
         company_5499 = create_company_5499(data_object)
         company.append(company_5499)
      elif legal_form in sarl_code: # SARL
         print(data_object)
         messages.warning(request,_('The companies with this legal structure are not compatible with the application at the moment.'))
      elif legal_form == "5480": # SAS
         print(data_object)
         print('Dans le 5480')
         messages.warning(request,_('The companies with this legal structure are not compatible with the application at the moment.'))    
      elif legal_form == "5710": # SA
         company_5410 = create_company_5710(data_object)
         company.append(company_5410)
      elif legal_form == "5760": # SCI
         print(data_object)
         pass
      elif legal_form == "5720": # SCP
         pass
      else:
         pass
    
    return company

