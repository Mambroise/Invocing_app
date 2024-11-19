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
            'hours','amount_excluding_tax', 'tax', 'attachment'
        ]

        widgets = {
            "due_date" : forms.DateInput(attrs={"type" : "date"})
        }

    # fields css    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = [
            'due_date', 'kind_of_payment',
            'hours','amount_excluding_tax', 'tax', 'attachment'
        ]

        for field_name in fields:
            self.fields[field_name].widget.attrs.update({
                'style': (
                    'padding: 5px; '
                    'border-radius: 5px; '
                    'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9); '
                    'transition: 0.5s;'
                ),
                'class': 'input-on-focus'
            })