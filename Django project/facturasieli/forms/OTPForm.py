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
