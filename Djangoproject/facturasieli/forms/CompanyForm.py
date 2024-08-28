# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/CompanyForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms

from facturasieli.models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['siret','name']
