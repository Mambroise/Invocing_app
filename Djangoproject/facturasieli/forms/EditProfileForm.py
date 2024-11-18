# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/EmailCheckForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms
from facturasieli.models import Profile,Role

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'avatar', 'email', 'first_name', 'last_name'
        ]
    
    # initialise differently the form according to the user role
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EditProfileForm, self).__init__(*args, **kwargs)
        

        # if user role == Company Manager or Admin, role is added to the form
        if self.user and self.user.has_role(['Admin']):
            self.fields['role'] = forms.ModelMultipleChoiceField(queryset=Role.objects.filter(id__in=[1,2,3]), required=True)
        
        # fields css
        fields = [
            'avatar', 'email', 'first_name', 'last_name','role'
        ]

        for field_name in fields:
            self.fields[field_name].widget.attrs.update({
                'style': (
                    'padding: 5px; '
                    'border-radius: 5px; '
                    'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9);'
                )
            })
            if field_name == 'email': 
                self.fields[field_name].widget.attrs.update({
                    'style': (
                        'padding: 5px; '
                        'border-radius: 5px; '
                        'box-shadow: 0 0 2px 2px rgba(135, 206, 250, 0.9); '
                        'width: 240px;'
                        'margin-left: 20px;'
                    )
                })

    def save(self, commit=True):
        profile = super(EditProfileForm, self).save(commit=False)
        
        if 'role' in self.cleaned_data and self.user.has_role(['Company manager', 'Admin']):
            profile.role.set(self.cleaned_data['role'])
        
        if commit:
            profile.save()
        
        return profile
