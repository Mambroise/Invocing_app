# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/OTPForm.py
# Author : Brice
# ---------------------------------------------------------------------------

from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from facturasieli.models import OTP


class OTPForm(ModelForm):
    class Meta:
        model = OTP
        fields = ['otp']
    
    # fields css
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['otp'].widget.attrs.update({
            'style': ('padding: 12px;'
                'border-radius: 5px;'
                'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9);'
                'transition: 0.5s;'
                'margin-left: 20px;'
            ),
            'class': 'input-on-focus'
        })
