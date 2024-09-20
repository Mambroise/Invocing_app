# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/ResetPasswordForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _
from facturasieli.validators import validate_pwd

class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(label=_('New password'),max_length=255,widget=forms.PasswordInput, validators=[validate_pwd])
    password2 = forms.CharField(label=_('Password confirmation'),widget=forms.PasswordInput,max_length=255)

    def clean_new_pwd2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("The two new passwords don't match"))
        return password2