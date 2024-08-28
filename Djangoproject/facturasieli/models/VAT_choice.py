
from django.db import models
from django.utils.translation import gettext as _

class VatChoice(models.IntegerChoices):
    FR_NORMAL_VAT = 1, _('20')
    FR_MEDIUM_vAT = 2, _('10')
    FR_LOW_VAT    = 3, _('5.5')
    FR_SPECIAL_VAT= 4, _('2.1')