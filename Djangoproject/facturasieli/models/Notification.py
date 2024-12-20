# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Notification.py
# Author : Arnaud, Zineb, Morice
# ---------------------------------------------------------------------------

from django.db import models
from django.utils.translation import gettext_lazy as _

from facturasieli.models.Company import Company
from facturasieli.models.NotificationType import NotificationType


class Notification(models.Model):
    send_at = models.DateField(_("Send At"))
    type = models.IntegerField(_("Type"), choices=NotificationType.choices, default=NotificationType.INVOICE_REQUEST)
    service_title = models.CharField(_("Service Title"), max_length=255)
    company_sender = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_sender')
    company_receiver = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_receiver')
    is_read = models.BooleanField(default=False)
    is_read_timestamp = models.DateTimeField(_("Opening time"), null=True)