# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/NotificationType.py
# Author : Arnaud, Zineb
# ---------------------------------------------------------------------------

from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationType(models.IntegerChoices):
    INVOICE_REQUEST = 1, _('Invoice Request')
    INVOICE_SUBMITTED = 2, _('Invoice Submitted')
    INVOICE_VERIFIED = 3, _('Invoice Verified')
    INVOICE_REJECTED = 4, _('Invoice Rejected')
    INVOICE_PAID = 5, _('Invoice Paid')
    INVOICE_MODIFIED = 6, _('Invoice Modified')
    INVOICE_DELETED = 7, _('Invoice Deleted')
    SERVICE_MODIFIED = 8, _('Service Modified')
    SERVICE_DELETED = 9, _('Service Deleted')

