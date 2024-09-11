# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/EmailCheckForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms

from facturasieli.models import Profile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'avatar','email','first_name','last_name','role'
        ]