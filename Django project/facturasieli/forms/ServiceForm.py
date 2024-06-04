# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/ServiceForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["title", "description", "intervention_start_date", "intervention_end_date", "company_provider"]  
        labels = {
            'title': _('Service Title:'),
            'description': _('Description:'),
            'intervention_start_date': _('Start of the service:'),
            'intervention_end_date': _('End of the service:'),
            'company_provider': _('Company:'),
        }
