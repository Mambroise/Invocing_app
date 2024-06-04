# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/NotificationType.py
# Author : Arnaud, Zineb
# ---------------------------------------------------------------------------

from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationType(models.IntegerChoices):
    DEMANDE_FACTURE = 1, _('Invoice Request')
    FACTURE_SOUMISE = 2, _('Invoice Submitted')
    FACTURE_VERIFIEE = 3, _('Invoice Verified')
    FACTURE_REJETEE = 4, _('Invoice Rejected')
    FACTURE_PAYEE = 5, _('Invoice Paid')
