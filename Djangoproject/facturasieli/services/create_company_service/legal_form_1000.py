# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/create_company_service/legal_form_1000.py
# Author : Morice
# ---------------------------------------------------------------------------

from facturasieli.models import Company,Address

def create_company_1000(data):
    # Extraire les données nécessaires de l'objet API
    data_personne_physique = data['formality']['content']['personnePhysique']

    siret = data['formality']['siren'] + data_personne_physique['identite']['entreprise']['nicSiege']
    
    name = data_personne_physique['etablissementPrincipal']['descriptionEtablissement'].get('nomCommercial')
    if not name:
        name = data_personne_physique['identite']['entrepreneur']['descriptionPersonne']['nom']
    activity = data_personne_physique['etablissementPrincipal']['activites'][0]['formeExercice']
    description = data_personne_physique['etablissementPrincipal']['activites'][0]['descriptionDetaillee']

    # address extraction
    address_data = data_personne_physique['etablissementPrincipal']['adresse']
    address = Address(
        country=address_data['pays'],
        zip_code=address_data['codePostal'],
        city=address_data['commune'],
        number=address_data['numVoie'],
        street=address_data['typeVoie']+' '+address_data['voie']
    )
    
    # Créer l'objet Company
    company = Company(
        siret=siret,
        name=name,
        activity=activity,
        description=description,
        address=address
    )
    
    return company

