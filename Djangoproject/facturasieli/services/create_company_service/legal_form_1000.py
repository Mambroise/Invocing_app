# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/create_company_service/create_company.py
# Author : Morice
# ---------------------------------------------------------------------------

from facturasieli.models import Company,Address

def create_company_1000(data):
    # Extraire les données nécessaires de l'objet API
    data_personne_physique = data['formality']['content']['personnePhysique']

    siret = data['formality']['siren'] + data_personne_physique['identite']['entreprise']['nicSiege']
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
#         "formeJuridique": "1000", personne physique
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

# {
#   "updatedAt": "2024-07-06T07:21:07+02:00",
#   "nombreRepresentantsActifs": 0,
#   "nombreEtablissementsOuverts": 0,
#   "id": "63ac691322b84a979c0388dd",
#   "formality": {
#     "siren": "751841404",
#     "content": {
#       "succursaleOuFiliale": "AVEC_ETABLISSEMENT",
#       "formeExerciceActivitePrincipale": "AGENT_COMMERCIAL",
#       "natureCreation": {
#         "dateCreation": "2012-06-06",
#         "societeEtrangere": false,
#         "formeJuridique": "1000",
#         "microEntreprise": false,
#         "etablieEnFrance": true,
#         "salarieEnFrance": true,
#         "relieeEntrepriseAgricole": false,
#         "entrepriseAgricole": false,
#         "eirl": false
#       },
#       "personnePhysique": {
#         "adresseEntreprise": {
#           "caracteristiques": {
#             "ambulant": false
#           },
#           "adresse": {
#             "roleAdressePresent": false,
#             "codePostalPresent": true,
#             "communePresent": true,
#             "codeInseeCommunePresent": true,
#             "typeVoiePresent": true,
#             "voiePresent": true,
#             "voieCodifieePresent": false,
#             "numVoiePresent": true,
#             "indiceRepetitionPresent": false,
#             "distributionSpecialePresent": false,
#             "communeAnciennePresent": false,
#             "rgpdPresent": false,
#             "datePriseEffetAdressePresent": false,
#             "complementLocalisationPresent": false,
#             "communeDeRattachementPresent": false,
#             "caracteristiquesPresent": false,
#             "indicateurValidationBANPresent": true,
#             "cedexPresent": false,
#             "pays": "FRANCE",
#             "codePays": "FRA",
#             "codePostal": "84000",
#             "commune": "AVIGNON",
#             "codeInseeCommune": "84007",
#             "typeVoie": "AV",
#             "voie": "DE LA CROIX DES OISEAUX",
#             "numVoie": "41"
#           }
#         },
#         "etablissementPrincipal": {
#           "descriptionEtablissement": {
#             "rolePourEntreprise": "3",
#             "siret": "75184140400021",
#             "nomCommercial": "ALLAIS XAVIER",
#             "indicateurEtablissementPrincipal": true,
#             "statutPourFormalite": "5",
#             "codeApe": "4321A",
#             "etablissementValidated": false,
#             "etablissementRdd": true
#           },
#           "adresse": {
#             "roleAdressePresent": false,
#             "codePostalPresent": true,
#             "communePresent": true,
#             "codeInseeCommunePresent": true,
#             "typeVoiePresent": true,
#             "voiePresent": true,
#             "voieCodifieePresent": false,
#             "numVoiePresent": true,
#             "indiceRepetitionPresent": false,
#             "distributionSpecialePresent": false,
#             "communeAnciennePresent": false,
#             "rgpdPresent": false,
#             "datePriseEffetAdressePresent": false,
#             "complementLocalisationPresent": false,
#             "communeDeRattachementPresent": false,
#             "caracteristiquesPresent": true,
#             "indicateurValidationBANPresent": true,
#             "cedexPresent": false,
#             "pays": "FRANCE",
#             "codePays": "FRA",
#             "codePostal": "84000",
#             "commune": "AVIGNON",
#             "codeInseeCommune": "84007",
#             "typeVoie": "AV",
#             "voie": "DE LA CROIX DES OISEAUX",
#             "numVoie": "41",
#             "caracteristiques": {
#               "ambulant": false
#             }
#           },
#           "activites": [
#             {
#               "categoryCode": "07121218",
#               "activiteId": "b1f413f8-ecd9-4e36-91ed-bf8066a6b060",
#               "indicateurPrincipal": true,
#               "indicateurProlongement": false,
#               "dateDebut": "2016-08-03",
#               "formeExercice": "AGENT_COMMERCIAL",
#               "categorisationActivite1": "07",
#               "categorisationActivite2": "12",
#               "categorisationActivite3": "12",
#               "categorisationActivite4": "18",
#               "codeAprm": "4321AB",
#               "descriptionDetaillee": "Travaux d'installation électrique dans tous locaux",
#               "indicateurActiviteeApe": true,
#               "indicateurArtisteAuteur": false,
#               "indicateurMarinProfessionnel": false,
#               "rolePrincipalPourEntreprise": true,
#               "codeApe": "4321A",
#               "activiteRattacheeEirl": false
#             }
#           ]
#         },
#         "autresEtablissements": [
#           {
#             "descriptionEtablissement": {
#               "rolePourEntreprise": "14",
#               "siret": "75184140400013",
#               "activiteNonSedentaire": false,
#               "indicateurEtablissementPrincipal": false,
#               "statutPourFormalite": "2",
#               "dateEffetFermeture": "2016-08-03",
#               "codeApe": "4321A",
#               "etablissementValidated": false,
#               "etablissementRdd": true
#             },
#             "adresse": {
#               "roleAdressePresent": false,
#               "codePostalPresent": true,
#               "communePresent": true,
#               "codeInseeCommunePresent": true,
#               "typeVoiePresent": true,
#               "voiePresent": true,
#               "voieCodifieePresent": false,
#               "numVoiePresent": true,
#               "indiceRepetitionPresent": true,
#               "distributionSpecialePresent": false,
#               "communeAnciennePresent": false,
#               "rgpdPresent": false,
#               "datePriseEffetAdressePresent": false,
#               "complementLocalisationPresent": false,
#               "communeDeRattachementPresent": false,
#               "caracteristiquesPresent": true,
#               "indicateurValidationBANPresent": true,
#               "cedexPresent": false,
#               "pays": "FRANCE",
#               "codePays": "FRA",
#               "codePostal": "84000",
#               "commune": "AVIGNON",
#               "codeInseeCommune": "84007",
#               "typeVoie": "AV",
#               "voie": "DE FONTCOUVERTE",
#               "numVoie": "3",
#               "indiceRepetition": "B",
#               "caracteristiques": {
#                 "ambulant": false
#               }
#             },
#             "activites": [
#               {
#                 "categoryCode": "05040200",
#                 "activiteId": "00249d20-f3e4-4fab-9476-5e482429cead",
#                 "indicateurPrincipal": true,
#                 "indicateurProlongement": false,
#                 "dateDebut": "2012-05-11",
#                 "exerciceActivite": "P",
#                 "indicateurNonSedentaire": false,
#                 "formeExercice": "ARTISANALE",
#                 "categorisationActivite1": "05",
#                 "categorisationActivite2": "04",
#                 "categorisationActivite3": "02",
#                 "codeAprm": "4321AB",
#                 "descriptionDetaillee": "ELECTRICIEN, PLOMBERIE, CLIMATISATION, SANITAIRE, CHAUFFAGE, ALARME, INST VIDEO SURVEILLANCE, DETECTION INCENDIE, AUTOMATISME",
#                 "indicateurActiviteeApe": false,
#                 "indicateurArtisteAuteur": false,
#                 "indicateurMarinProfessionnel": false,
#                 "rolePrincipalPourEntreprise": false,
#                 "codeApe": "4321A",
#                 "activiteRattacheeEirl": false,
#                 "origine": {
#                   "typeOrigine": "1"
#                 },
#                 "locataireGerantMandataire": {
#                   "mandat": "0"
#                 }
#               }
#             ],
#             "registreAnterieur": {
#               "raa": {
#                 "estPresent": false
#               },
#               "rnm": {
#                 "estPresent": true,
#                 "dateDebut": "2012-05-11T00:00:00+02:00"
#               },
#               "rncs": {
#                 "estPresent": false
#               }
#             }
#           }
#         ],
#         "identite": {
#           "adresseCorrespondancePresent": false,
#           "entreprise": {
#             "siren": "751841404",
#             "formeJuridique": "1000",
#             "nicSiege": "00021",
#             "codeApe": "4321A",
#             "dateImmat": "2012-06-06",
#             "
