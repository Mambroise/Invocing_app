# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/SearchForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _

class SearchForm(forms.Form):
    search = forms.CharField(max_length=60, required=True)

    # fields css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs.update({
            'style': ('padding: 12px;'
                'border-radius: 5px;'
                'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9);'
                'transition: 0.5s;'
            ),
            'class': 'input-on-focus'
        })
