# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/send_email.py
# Author : Morice
# ---------------------------------------------------------------------------

from facturasieli.models import Company,Address

def create_company_from_api_data(data):
    # Extraire les données nécessaires de l'objet API
    data_personne_physique = data['formality']['content']['personnePhysique']
    siret = data['formality']['siren'] + data_personne_physique['identite']['entreprise']['nicSiege']
    name = data_personne_physique['identite']['entrepreneur']['descriptionPersonne']['nomUsage']

    # Extraire l'adresse
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
        address=address
    )
    
    return company
# {
#   "updatedAt": "2024-07-06T20:19:09+02:00",
#   "nombreRepresentantsActifs": 0,
#   "nombreEtablissementsOuverts": 0,
#   "id": "63cfcc542e42d5caec06b445",
#   "formality": {
#     "siren": "899377568",
#     "content": {
#       "succursaleOuFiliale": "AVEC_ETABLISSEMENT",
#       "formeExerciceActivitePrincipale": "GESTION_DE_BIENS",
#       "natureCreation": {
#         "dateCreation": "2020-03-03",
#         "formeJuridique": "1000",
#         "microEntreprise": false,
#         "relieeEntrepriseAgricole": false,
#         "entrepriseAgricole": false,
#         "eirl": false
#       },
#       "personnePhysique": {
#         "adresseEntreprise": {
#           "adresse": {
#             "pays": "FRANCE",
#             "codePays": "FRA",
#             "codePostal": "77300",
#             "commune": "FONTAINEBLEAU",
#             "codeInseeCommune": "77186",
#             "typeVoie": "RUE",
#             "voie": "GRANDE",
#             "numVoie": "109"
#           }
#         },
#         "etablissementPrincipal": {
#           "descriptionEtablissement": {
#             "rolePourEntreprise": "3",
#             "siret": "89937756800014",
#             "indicateurEtablissementPrincipal": true,
#             "statutPourFormalite": "5",
#             "codeApe": "6820A",
#             "etablissementValidated": false,
#             "etablissementRdd": true
#           },
#           "adresse": {
#             "pays": "FRANCE",
#             "codePays": "FRA",
#             "codePostal": "77300",
#             "commune": "FONTAINEBLEAU",
#             "codeInseeCommune": "77186",
#             "typeVoie": "RUE",
#             "voie": "GRANDE",
#             "numVoie": "109"
#           },
#           "activites": [
#             {
#               "categoryCode": "07060101",
#               "activiteId": "91de4967-335c-4a53-b584-379b12c5ed33",
#               "indicateurPrincipal": true,
#               "indicateurProlongement": false,
#               "dateDebut": "2020-03-03",
#               "formeExercice": "GESTION_DE_BIENS",
#               "categorisationActivite1": "07",
#               "categorisationActivite2": "06",
#               "categorisationActivite3": "01",
#               "categorisationActivite4": "01",
#               "descriptionDetaillee": "Location de logements",
#               "indicateurActiviteeApe": true,
#               "indicateurArtisteAuteur": false,
#               "indicateurMarinProfessionnel": false,
#               "rolePrincipalPourEntreprise": true,
#               "codeApe": "6820A",
#               "activiteRattacheeEirl": false
#             }
#           ]
#         },
#         "identite": {
#           "entreprise": {
#             "siren": "899377568",
#             "formeJuridique": "1000",
#             "nicSiege": "00014",
#             "codeApe": "6820A",
#             "dateImmat": "2020-03-03",
#             "dateDebutActiv": "2020-03-03",
#             "entrepriseValidated": false,
#             "entrepriseRdd": true
#           },
#           "entrepreneur": {
#             "descriptionPersonne": {
#               "nom": "N'GUESSAN",
#               "prenoms": ["DALY", "KOUASSI"],
#               "genre": "1",
#               "nomUsage": "N'GUESSAN FOUCHE"
#             }
#           }
#         }
#       }
#     }
#   },
#   "diffusionINSEE": "N",
#   "typePersonne": "P",
#   "diffusionCommerciale": true,
#   "formeJuridique": "1000",
#   "siren": "899377568"
# }
