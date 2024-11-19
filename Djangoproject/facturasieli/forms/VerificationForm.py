# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/VerificationForm.py
# Author : Zineb, Morice
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Verification


class VerificationForm(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ['comments']

    STATUS_CHOICES = [
        (2, _('Confirm')),# 2 corresponds to invoice.status "verified"
        (3, _('reject'))# 3 corresponds to invoice.status "Rejected"
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect)

    # fields css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comments'].widget.attrs.update({
            'style': ('padding: 5px;'
                'border-radius: 5px;'
                'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9);'
                'transition: 0.5s;'
                'margin-left: 20px;'
            ),
            'class': 'input-on-focus'
        })
    