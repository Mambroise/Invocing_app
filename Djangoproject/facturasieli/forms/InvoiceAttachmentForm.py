from django import forms
from facturasieli.models import Invoice

class InvoiceAttachmentForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['attachment'] 