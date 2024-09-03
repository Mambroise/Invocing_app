# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Invoice.py
# Author : Arnaud, Zineb
# ---------------------------------------------------------------------------

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Address,VAT_choice


class Invoice(models.Model):
    STATUS_CHOICES = [
        (1, _('Pending')),
        (2, _('Verified')),
        (3, _('Rejected')),
        (4, _('Paid'))
    ]

    invoice_number = models.IntegerField(_("Invoice Number"),null=True,unique=True)
    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField(_("Due Date"))
    kind_of_payment = models.CharField(_("Kind of Payment"), max_length=255, default=_('Bank Transfer'))
    name_provider = models.CharField(_("Provider Name"), max_length=255)
    name_client = models.CharField(_("Client Name"), max_length=255)
    hours = models.FloatField(_("Hours worked"),help_text=_("<small style='display:block;'>worked minutes are counted as followed: 15 mins = 0.25 hour.</small>"),null=True)
    amount_excluding_tax = models.FloatField(_("Amount Excluding Tax"))
    tax = models.FloatField(_("Tax"), choices=VAT_choice.VatChoice)
    status = models.CharField(_("Status"), max_length=50, choices=STATUS_CHOICES, default=1)
    provider_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='invoices_as_provider')
    client_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='invoices_as_client')
    update_timestamp = models.DateTimeField(_("Time of update"),null=True)
    attachment = models.FileField(_('BIS'),upload_to="BIS/", null=True,blank=True)


    def __str__(self):
        return f'Invoice {self.invoice_number} - {self.status}'
