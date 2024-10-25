# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/create_company_service/create_company.py
# Author : Morice
# ---------------------------------------------------------------------------

from facturasieli.services.create_company_service.legal_form_1000 import create_company_1000
from facturasieli.models import Company,Address

def create_company_from_api_data(data):

    company = None
    # Extraire les données nécessaires de l'objet API
    legal_form = data['formality']['content']['natureCreation']['formeJuridique']
    if legal_form == "1000": # personne physique
      company = create_company_1000(data)
    elif legal_form == "5499": # Autre societe civile
       pass
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


# {
#   "updatedAt": "2024-05-18T21:50:26+02:00",
#   "nombreRepresentantsActifs": 1,
#   "nombreEtablissementsOuverts": 0,
#   "id": "63ac632ae3573db1981008ad",
#   "formality": {
#     "siren": "750526709",
#     "content": {
#       "succursaleOuFiliale": "AVEC_ETABLISSEMENT",
#       "formeExerciceActivitePrincipale": "COMMERCIALE",
#       "natureCreation": {
#         "dateCreation": "2012-04-06",
#         "societeEtrangere": false,
#         "formeJuridique": "5499", Autre societe civile
#         "microEntreprise": false,
#         "etablieEnFrance": true,
#         "salarieEnFrance": true,
#         "relieeEntrepriseAgricole": false,
#         "entrepriseAgricole": false,
#         "eirl": false
#       },
#       "personneMorale": {
#         "adresseEntreprise": {
#           "caracteristiques": {
#             "ambulant": false,
#             "domiciliataire": false
#           },
#           "adresse": {
#             "pays": "FRANCE",
#             "codePays": "FRA",
#             "codePostal": "84100",
#             "commune": "ORANGE",
#             "codeInseeCommune": "84087",
#             "typeVoie": "RUE",
#             "voie": "D'IRLANDE",
#             "numVoie": "117"
#           }
#         },
#         "etablissementPrincipal": {
#           "descriptionEtablissement": {
#             "rolePourEntreprise": "2",
#             "pays": "FRANCE",
#             "codePays": "FRA",
#             "siret": "75052670900027",
#             "activiteNonSedentaire": false,
#             "nomCommercial": "PLOMBERIE ELECTRICITE CHAUFFAGE SANITAIRE CLIMATISATION RECHERCHES DE",
#             "indicateurEtablissementPrincipal": true,
#             "statutPourFormalite": "5",
#             "codeApe": "4322A",
#             "etablissementValidated": false,
#             "etablissementRdd": true
#           },
#           "adresse": {
#             "pays": "FRANCE",
#             "codePays": "FRA",
#             "codePostal": "84100",
#             "commune": "ORANGE",
#             "codeInseeCommune": "84087",
#             "typeVoie": "RUE",
#             "voie": "D'IRLANDE",
#             "numVoie": "117"
#           },
#           "activites": [
#             {
#               "categoryCode": "05040200",
#               "activiteId": "ee419f94-cf0e-4efb-9e41-a48a73717486",
#               "indicateurPrincipal": true,
#               "dateDebut": "2012-04-01",
#               "exerciceActivite": "P",
#               "formeExercice": "COMMERCIALE",
#               "codeApe": "4322A",
#               "descriptionDetaillee": "Plomberie électricité chauffage sanitaire climatisation recherchés de fuites assainissement terrassement installations de piscines Vrd avec mini pelle location de matériel d'équipement sanitaire (lavabos, water-closets, etc.) Sous le nom de 'VC Location'"
#             },
#             {
#               "categoryCode": "05040300",
#               "activiteId": "fc141c96-54c6-4e81-b9d9-9bffa4f52f47",
#               "indicateurPrincipal": false,
#               "dateDebut": "2012-04-01",
#               "exerciceActivite": "P",
#               "formeExercice": "ARTISANALE_REGLEMENTEE",
#               "codeApe": "4322A",
#               "descriptionDetaillee": "PLOMBERIE ELECTRICITE CHAUFFAGE SANITAIRE CLIMATISATION RECHERCHES DE FUITES ASSAINISSEMENT TERRASSEMENT INSTALLATIONS DE PISCINES VRD"
#             }
#           ],
#           "registreAnterieur": {
#             "raa": {
#               "estPresent": false
#             },
#             "rnm": {
#               "estPresent": true,
#               "dateDebut": "2019-02-22T00:00:00+01:00"
#             },
#             "rncs": {
#               "estPresent": true,
#               "dateDebut": "2012-04-01T00:00:00+02:00"
#             }
#           }
#         },
#         "autresEtablissements": [
#           {
#             "descriptionEtablissement": {
#               "rolePourEntreprise": "14",
#               "siret": "75052670900019",
#               "nomCommercial": "PLOMBERIE ELECTRICITE CHAUFFAGE SANITAIRE CLIMATISATION RECHERCHES DE",
#               "indicateurEtablissementPrincipal": false,
#               "statutPourFormalite": "2",
#               "dateEffetFermeture": "2019-02-22",
#               "codeApe": "4322A"
#             },
#             "adresse": {
#               "pays": "FRANCE",
#               "codePays": "FRA",
#               "codePostal": "84100",
#               "commune": "ORANGE",
#               "codeInseeCommune": "84087",
#               "typeVoie": "CHE",
#               "voie": "DE CHAMPLAIN",
#               "complementLocalisation": "LE HAUT ABRIAN"
#             },
#             "activites": [
#               {
#                 "categoryCode": "05040300",
#                 "activiteId": "9ac9a0c7-acb1-4d94-b2b5-c08796636974",
#                 "indicateurPrincipal": true,
#                 "dateDebut": "2012-03-01",
#                 "dateFin": "2019-02-22",
#                 "exerciceActivite": "P",
#                 "formeExercice": "ARTISANALE_REGLEMENTEE",
#                 "codeApe": "4322A",
#                 "descriptionDetaillee": "PLOMBERIE ELECTRICITE CHAUFFAGE SANITAIRE CLIMATISATION RECHERCHES DE FUITES ASSAINISSEMENT TERRASSEMENT INSTALLATIONS DE PISCINES"
#               }
#             ],
#             "detailCessationEtablissement": {
#               "dateCessationTotaleActivite": "2019-02-22"
#             },
#             "registreAnterieur": {
#               "rnm": {
#                 "estPresent": true,
#                 "dateDebut": "2012-03-01T00:00:00+01:00",
#                 "dateFin": "2019-02-22T00:00:00+01:00"
#               }
#             }
#           }
#         ],
#         "composition": {
#           "pouvoirs": [
#             {
#               "roleEntreprise": "30",
#               "typeDePersonne": "INDIVIDU",
#               "indicateurActifAgricole": false,
#               "representantId": "4fc4357f-e4cd-4b48-9b74-41ece0c98560",
#               "individu": {
#                 "descriptionPersonne": {
#                   "dateDeNaissance": "1971-05",
#                   "nom": "CHAMBON",
#                   "prenoms": ["CHRISTOPHE"],
#                   "genre": "1",
#                   "nationalite": "Française"
#                 },
#                 "adresseDomicile": {
#                   "pays": "FRANCE",
#                   "codePays": "FRA",
#                   "codePostal": "84100",
#                   "commune": "Orange",
#                   "codeInseeCommune": "84087"
#                 },
#                 "qualiteArtisan": "ARTISAN",
#                 "actif": true
#               }
#             }
#           ]
#         },
#         "identite": {
#           "entreprise": {
#             "siren": "750526709",
#             "denomination": "CHRISTOPHE CHAMBON",
#             "formeJuridique": "5499",
#             "nicSiege": "00027",
#             "nomCommercial": "PLOMBERIE ELECTRICITE CHAUFFAGE SANITAIRE CLIMATISATION RECHERCHES DE",
#             "codeApe": "4322A",
#             "dateImmat": "2012-04-06",
#             "effectifSalarie": 3,
#             "dateDebutActiv": "2012-03-01"
#           },
#           "description": {
#             "objet": "Plomberie électricité chauffage sanitaire climatisation recherchés de fuites assainissement terrassement installations de piscines Vrd avec mini pelle location de matériel d'équipement sanitaire (lavabos, water-closets, etc.) Sous le nom de 'VC Location'",
#             "duree": 99,
#             "dateClotureExerciceSocial": "3009",
#             "datePremiereCloture": "2012-09-30",
#             "capital": {
#               "montant": 13090.0,
#               "devise": "EUR"
#             }
#           }
#         },
#         "registreAnterieur": {
#           "rnm": {
#             "estPresent": true,
#             "dateDebut": "2019-02-22T00:00:00+01:00"
#           },
#           "rncs": {
#             "estPresent": true,
#             "dateDebut": "2012-04-06T00:00:00+02:00"
#           }
#         }
#       }
#     }
#   }
# }
