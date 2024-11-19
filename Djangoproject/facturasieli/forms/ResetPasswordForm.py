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

    def __init__(self, request, *args, **kwargs):
        """Add old_password field if user is authenticated."""
        self.request = request
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

        # If the user is authenticated, add the old_password field
        if request.user.is_authenticated:
            self.fields['old_password'] = forms.CharField(
                label=_('Current password'),
                widget=forms.PasswordInput,
                max_length=255
            )

        fields = ['password1','password2','old_password']
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

    def clean_old_password(self):
        if self.request.user.is_authenticated:
            old_password = self.cleaned_data.get('old_password')
            if not self.request.user.check_password(old_password):
                raise forms.ValidationError(_('Your current password is incorrect.'))
            return old_password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("The two new passwords don't match"))
        return password2