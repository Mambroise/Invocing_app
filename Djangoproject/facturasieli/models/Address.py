# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Address.py
# Author : Arnaud, Zineb
# ---------------------------------------------------------------------------

from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    number = models.IntegerField(_("Number"))
    street = models.CharField(_("Street"), max_length=255)
    addings = models.CharField(_("Addings"), max_length=255, blank=True, null=True)
    zip_code = models.IntegerField(_("Zip Code"))
    city = models.CharField(_("City"), max_length=255)
    country = models.CharField(_("Country"), max_length=255)

    def __str__(self):
        return f'{self.number} {self.street}, {self.city}, {self.country}'
