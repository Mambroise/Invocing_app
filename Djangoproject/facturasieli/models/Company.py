# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Company.py
# Author : Arnaud, Zineb
# ---------------------------------------------------------------------------

from django.db import models
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Address
from facturasieli.validators import validate_phone_number


class Company(models.Model):
    siret = models.CharField(_("SIRET"), max_length=15)
    name = models.CharField(_("Name"), max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='companies')
    phone = models.CharField(_('Phone number'), max_length=15, null=True, validators=[validate_phone_number])

    def __str__(self):
        return self.name
