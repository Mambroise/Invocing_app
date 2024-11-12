# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/create_company_service/get_from_data.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.utils.translation import gettext_lazy as _
from facturasieli.models import Address,Company

def get_address(data):
    
    address = Address(
        country=data['pays'],
        zip_code=data['codePostal'],
        city=data['commune'],
        number=data.get('numVoie'),
        street=(data.get('typeVoie', '') + ' ' + data.get('voie', '')).strip()
    )

    if address.number is None:
        address.number = ''
    return address


#get the name in the complex json object according to the company legal form and the way it was registered
def get_company_name (data):

    legal_form = data['formality']['content']['natureCreation']['formeJuridique']

    if legal_form == '1000':
        data_personne_physique = data['formality']['content']['personnePhysique']

        name = data_personne_physique['etablissementPrincipal']['descriptionEtablissement'].get('nomCommercial')
        if not name:
            name = data_personne_physique['identite']['entrepreneur']['descriptionPersonne'].get('nom')
    else:
        data_personne_morale = data['formality']['content']['personneMorale']

        name = data_personne_morale['etablissementPrincipal']['descriptionEtablissement'].get('nomCommercial')
        if not name:
            name = data_personne_morale['etablissementPrincipal']['descriptionEtablissement'].get('enseigne')
    if not name:
        try:
            name = data_personne_morale['identite']['entrepreneur']['denomination']
        except Exception as e:
            print('error create_company_5499:',e)
            name = _('please determin')

    return name

def get_companies_from_list(data):
    companies = []

    for data_object in data:
        siret = data_object['descriptionEtablissement'].get('siret')
        name = data_object['descriptionEtablissement'].get('enseigne')
        if name == None:
            name = ''

        activity = data_object['activites'][0].get('formeExercice')


        description = data_object['activites'][0].get('descriptionDetaillee')

        address_data = data_object['adresse']
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

    return companies