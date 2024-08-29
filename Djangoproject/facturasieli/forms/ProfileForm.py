# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/ProfileForm.py
# Author : Zineb
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _
from facturasieli.models import Profile, Role

class ProfileForm(forms.ModelForm):
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)
    role = forms.ModelMultipleChoiceField(queryset=Role.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)

    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'role')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Filtrer les rôles par ID pour n'afficher que les rôles souhaités
        self.fields['role'].queryset = Role.objects.filter(id__in=[2, 3, 4])

        translated_choices = []
        for role in self.fields['role'].queryset:
            translated_name = _(role.role)  
            translated_choices.append((role.id, translated_name))
        
        # creation of variable for i18n in .po file
        provider = _("Provider")
        Company_Manager = _("Company Manager")
        Company_Verifier = _("Company Verifier")

        self.fields['role'].choices = translated_choices

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.set_password(self.cleaned_data["password1"])
        if commit:
            profile.save()
            self.save_m2m()  # Save the many-to-many data for roles
        return profile

