# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/CompanyForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['siret','name', 'activity', 'description', 'phone']
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
        
    # fields css  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        names_to_determin = ['please determin', 'A déterminer']
        if self.fields['name'] not in names_to_determin:
            readonly_fields = ['siret', 'name', 'activity', 'description']
        else:
            readonly_fields = ['siret', 'activity', 'description']
        
        for field_name in readonly_fields:
            self.fields[field_name].widget.attrs.update({
                'style': (
                'padding: 5px; '
                'border-radius: 5px; '
                'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9); '
                )
            })
            self.fields[field_name].widget.attrs['readonly'] = True

            self.fields['phone'].widget.attrs.update({
                'style': (
                'padding: 5px; '
                'border-radius: 5px; '
                'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9); '
                )
            })
            
