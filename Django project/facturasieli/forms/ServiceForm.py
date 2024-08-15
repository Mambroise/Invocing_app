# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/forms/ServiceForm.py
# Author : Morice
# ---------------------------------------------------------------------------

from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from facturasieli.models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["title", "description", "intervention_start_date", "intervention_end_date"]  
        labels = {
            'title': _('Service Title:'),
            'description': _('Description:'),
            'intervention_start_date': _('Start of the service:'),
            'intervention_end_date': _('End of the service:'),

        }
        widgets = {
            "intervention_start_date" : forms.DateInput(attrs={"type" : "date"}),
            "intervention_end_date" : forms.DateInput(attrs={"type" : "date"})
        }

    def clean(self):
        cleaned_data = super().clean()
        intervention_start_date = cleaned_data.get("intervention_start_date")
        intervention_end_date = cleaned_data.get("intervention_end_date")

        if intervention_start_date and intervention_end_date and intervention_end_date < intervention_start_date:
            raise ValidationError({
                'intervention_end_date': _('End of the service cannot be before the start of the service.')
            })
        
        return cleaned_data
