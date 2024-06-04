# FacturaSieli
Application de suivi de facturation.

## Architecture de l'application

### Front-end :
* HTML
* CSS
* JS

### Back-end :
* Frameworks : Django (Python).
* Base de données : SQLite, PostgreSQL, MySQL ou MongoDB pour stocker les données des factures, utilisateurs, et états des vérifications.

## Sécurité :
### Authentification :
* JWT (JSON Web Token) pour des sessions sécurisées.

### Autorisations :
* Gestion des rôles (sous-traitants, service de vérification, comptabilité) pour contrôler l'accès aux différentes parties de l'application.

## Modules et fonctionnalités :
### 1. Module "Sous-traitants"
Fonctionnalités :
* Soumission des factures :\
  Formulaire pour créer et soumettre une facture avec les détails nécessaires (description du travail, montant, date).
* Suivi des factures :\
  Interface pour voir le statut des factures soumises (en attente, vérifiée, payée).
* Notification :\
  Alertes par email ou notification in-app pour les mises à jour du statut de leurs factures.

### 2. Module "Service de Vérification"
Fonctionnalités :
* Liste des factures à vérifier :\
  Tableau de bord montrant les factures soumises par les sous-traitants.
* Détail de la facture :\
  Interface pour voir et éditer les détails de chaque facture.
* Validation/Réjection :\
  Boutons pour marquer les factures comme vérifiées ou rejetées avec la possibilité d’ajouter des commentaires.
* Historique des vérifications :\
  Suivi des actions de vérification pour chaque facture (qui a vérifié quoi et quand).

### 3. Module "Comptabilité"
Fonctionnalités :
* Liste des factures vérifiées :\
  Tableau de bord avec les factures prêtes à être payées.
* Détail de la facture :\
  Interface pour voir les informations de la facture et l'état de la vérification.
* Historique des paiements :\
  Journal des paiements effectués avec des détails (facture, date, montant, méthode de paiement).
