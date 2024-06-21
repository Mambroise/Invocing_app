# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/VerificationForm.py
# Author : Zineb, Morice
# ---------------------------------------------------------------------------

from django import forms

from facturasieli.models import Verification


class VerificationForm(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ['comments']

    STATUS_CHOICES = [
        (2, 'Verified'),# 2 corresponds to invoice.status "verified"
        (3, 'rejected')# 3 corresponds to invoice.status "Rejected"
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect)
    