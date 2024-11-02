# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/create_company_service/legal_form_5499.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.utils.translation import gettext_lazy as _
from facturasieli.models import Company
from facturasieli.services.create_company_service.get_from_data import get_address,get_company_name


def create_company_5499(data):
    # extract data from api json object
    data_personne_morale = data['formality']['content']['personneMorale']

    siret = data['formality']['siren'] + data_personne_morale['identite']['entreprise']['nicSiege']
    
    name = get_company_name(data)
    activity = data_personne_morale['etablissementPrincipal']['activites'][0]['formeExercice']
    description = data_personne_morale['etablissementPrincipal']['activites'][0]['descriptionDetaillee']

    # address extraction
    address_data = data_personne_morale['etablissementPrincipal']['adresse']
    address = get_address(address_data)
    
    # Créer l'objet Company
    company = Company(
        siret=siret,
        name=name,
        activity=activity,
        description=description,
        address=address
    )
    
    return company

