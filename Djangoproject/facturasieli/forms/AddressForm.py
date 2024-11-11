# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/AddressForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from facturasieli.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['number','street','addings','zip_code','city','country']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number'].widget.attrs.update({'style': 'width: 60px;'})
        self.fields['zip_code'].widget.attrs.update({'style': 'width: 80px;'})

        readonly_fields = ['number','street','addings','zip_code','city','country']
        for field_name in readonly_fields:
            self.fields[field_name].widget.attrs['readonly'] = True

        