# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Verification.py
# Author : Arnaud, Zineb
# ---------------------------------------------------------------------------

from django.db import models
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Invoice, Profile


class Verification(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='verifications')
    verified_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='verifications_user')
    date_verified = models.DateTimeField(_("Date Verified"), auto_now_add=True)
    comments = models.TextField(_("Comments"))

    def __str__(self):
        return f"{self.invoice.invoice_number} by {self.verified_by.email}"
