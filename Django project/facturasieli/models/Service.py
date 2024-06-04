# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Service.py
# Author : Arnaud, Zineb
# ---------------------------------------------------------------------------

from django.db import models
from django.utils.translation import gettext_lazy as _

from facturasieli.models.Company import Company
from facturasieli.models.Invoice import Invoice


class Service(models.Model):
    DEMANDE_DE_FACTURATION_ENVOYEE = _('Invoice Request Sent')
    TERMINE = _('Closed')
    STATUS_CHOICES = [
        (DEMANDE_DE_FACTURATION_ENVOYEE, _('Invoice Request Sent')),
        (TERMINE, _('Closed'))
    ]

    title = models.CharField(_("Title"), max_length=255)
    description = models.CharField(_("Description"), max_length=255)
    issue_date = models.DateField(_("Issue Date"))
    intervention_start_date = models.DateField(_("Intervention Start Date"))
    intervention_end_date = models.DateField(_("Intervention End Date"))
    status = models.CharField(_("Status"), max_length=50, choices=STATUS_CHOICES, default=DEMANDE_DE_FACTURATION_ENVOYEE)
    company_provider = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='provided_services')
    company_client = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='received_services')
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, related_name='service', null=True, blank=True)

    def __str__(self):
        return self.title
