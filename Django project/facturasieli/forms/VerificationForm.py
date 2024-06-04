# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/VerificationForm.py
# Author : Zineb
# ---------------------------------------------------------------------------

from django import forms

from facturasieli.models import Verification


class VerificationForm(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ['comments']

    STATUS_CHOICES = [
        (1, 'Verified'),
        (2, 'rejected')
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect)
    