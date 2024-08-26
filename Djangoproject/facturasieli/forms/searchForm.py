# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/SearchForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _

class SearchForm(forms.Form):
    search = forms.CharField(max_length=60,required=True)