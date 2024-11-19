# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/EmailCheckForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _

class EmailCheckForm(forms.Form):
    email = forms.EmailField(label=_('Email'))

    # fields css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'style': ('padding: 12px;'
                'border-radius: 5px;'
                'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9);'
                'transition: 0.5s;'
                'margin-left: 20px;'
                'width: 240px;'
            ),
            'class': 'input-on-focus'
        })