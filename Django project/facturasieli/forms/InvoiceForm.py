# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/InvoiceForm.py
# Author : Margaux
# ---------------------------------------------------------------------------

from django import forms

from facturasieli.models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'invoice_number', 'issue_date', 'due_date', 'kind_of_payment',
            'name_client', 'amount_excluding_tax', 'tax',
            'status'
        ]
