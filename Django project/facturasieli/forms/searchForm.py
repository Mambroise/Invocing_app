from django import forms
from django.utils.translation import gettext_lazy as _

class SearchForm(forms.Form):
    search = forms.CharField(max_length=60,required=True)