# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/ResetPasswordForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _

class ResetPasswordForm(forms.Form):
    new_pwd = forms.CharField(label=_('New password'),max_length=255)
    new_pwd2 = forms.CharField(label=_('Password confirmation'),max_length=255)

    def clean_new_pwd2(self):
        new_pwd = self.cleaned_data.get('new_pwd')
        new_pwd2 = self.cleaned_data.get('new_pwd2')
        if new_pwd and new_pwd2 and new_pwd != new_pwd2:
            raise forms.ValidationError(_("The two new passwords don't match"))
        return new_pwd2