# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/ResetPasswordForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _

class ResetPasswordForm(forms.Form):
    old_pwd = forms.CharField(label=_('Old password'))
    new_pwd = forms.CharField(label=_('New password'))
    new_pwd2 = forms.CharField(label=_('Repeat new password'))