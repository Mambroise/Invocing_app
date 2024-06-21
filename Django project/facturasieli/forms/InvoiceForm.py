# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/InvoiceForm.py
# Author : Margaux, Morice
# ---------------------------------------------------------------------------

from django import forms

from facturasieli.models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'due_date', 'kind_of_payment',
            'hours','amount_excluding_tax', 'tax'
        ]

        widgets = {
            "due_date" : forms.DateInput(attrs={"type" : "date"})
        }
        
