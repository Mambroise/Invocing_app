# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/create_company_service/legal_form_5710.py
# Author : Morice
# ---------------------------------------------------------------------------

from facturasieli.models import Company
from facturasieli.services.create_company_service.get_from_data import get_address,get_company_name,get_companies_from_list
from django.utils.translation import gettext_lazy as _

def create_company_5710(data):

    companies = []
    # extract data from api json object
    data_personne_morale = data['formality']['content']['personneMorale']

    if data_personne_morale.get('etablissementPrincipal') != None:
        siret = data_personne_morale['etablissementPrincipal']['descriptionEtablissement'].get('siret')

        name = get_company_name(data)
        activity = data_personne_morale['etablissementPrincipal']['activites'][0].get('formeExercice')
        description = data_personne_morale['etablissementPrincipal']['activites'][0].get('descriptionDetaillee')

        # address extraction
        address_data = data_personne_morale['etablissementPrincipal'].get('adresse')
        address = get_address(address_data)

    # Create Company object 
    company = Company(
        siret=siret,
        name=name,
        activity=activity,
        description=description,
        address=address
    )
    companies.append(company)

    if len(data_personne_morale['autresEtablissements']) >1:
        companies_data = data_personne_morale['autresEtablissements']
        company_list = get_companies_from_list(companies_data)

        companies.extend(company_list)
    
    return companies

