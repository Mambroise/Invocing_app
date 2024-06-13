# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/AddressForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms

from facturasieli.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['number','street','addings','zip_code','city','country']