from django import forms
from facturasieli.models import Invoice

class InvoiceAttachmentForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['attachment'] 

    # fields css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attachment'].widget.attrs.update({
            'style': (
                'border-radius: 5px;'
                'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9);'
                'transition: 0.5s;'
                'margin-left: 20px;'
            ),
            'class': 'input-on-focus'
        })