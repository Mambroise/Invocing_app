# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/CompanyForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['siret','name', 'phone']
        error_messages = {
            'siret': {
                'required': _("SIRET number is required."),
                'invalid': _("Enter a valid SIRET number."),
                'max_length':_("SIRET number requires 14 numbers")
            },
            'name': {
                'required': _("Company name is required."),
            },
            'phone': {
                'invalid': _("Enter a valid phone number."),
            }
        }
