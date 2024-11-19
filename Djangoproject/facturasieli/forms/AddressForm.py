# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/AddressForm.py
# Author : Morice
# ---------------------------------------------------------------------------


from django import forms
from facturasieli.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['number','street','addings','zip_code','city','country']

    # fields css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = ['number','street','addings','zip_code','city','country']

        for field_name in fields:
            self.fields[field_name].widget.attrs.update({
                'style':(
                    'padding: 5px; '
                    'border-radius: 5px; '
                    'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9); '
                    'transition: 0.5s;'   
                ),
                'class': 'input-on-focus'
            })
            if field_name == 'number':
                self.fields[field_name].widget.attrs.update({
                'style':(
                    'padding: 5px; '
                    'border-radius: 5px; '
                    'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9); '
                    'transition: 0.5s;'
                    'width: 60px;'   
                ),
                'class': 'input-on-focus'
            })
            elif field_name == 'zip_code':
                self.fields[field_name].widget.attrs.update({
                'style':(
                    'padding: 5px; '
                    'border-radius: 5px; '
                    'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9); '
                    'transition: 0.5s;'
                    'width: 80px;'   
                ),
                'class': 'input-on-focus'
            })
            self.fields[field_name].widget.attrs['readonly'] = True

        