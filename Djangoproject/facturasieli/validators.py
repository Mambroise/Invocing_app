# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/validators.py
# Author : Morice
# ---------------------------------------------------------------------------

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone_number(value):
    if not re.match(r'^\+?1?\d{9,15}$', value):
        raise ValidationError(_('Invalid phone number format.'))
    
def validate_siret(value):
    if not re.match(r'^\d{14}$', value):
        raise ValidationError(_('Siret requires 14 numbers'))
    
def validate_pwd(value):
    if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{10,}$', value):
        raise ValidationError(_('Invalid password'))

