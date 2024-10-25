# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Company.py
# Author : Moris, Zineb
# ---------------------------------------------------------------------------

from django.db import models
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Address
from facturasieli.validators import validate_phone_number,validate_siret


class Company(models.Model):
    siret = models.CharField(_("SIRET"), max_length=15, validators=[validate_siret])
    name = models.CharField(_("Name"), max_length=255)
    activity = models.CharField(_('Activity'), max_length=255,null=True)
    description = models.CharField(_('Activity'), max_length=255,null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='companies')
    phone = models.CharField(_('Phone number'), max_length=15, null=True, validators=[validate_phone_number])

    def __str__(self):
        return self.name
