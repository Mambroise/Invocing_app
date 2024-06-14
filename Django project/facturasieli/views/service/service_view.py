# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/service_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Service


def display_service(request, company_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    client_services = Service.objects.filter(company_client=company_id)
    provider_services = Service.objects.filter(company_provider=company_id)

    if not client_services and not provider_services:
        return HttpResponseRedirect(reverse('facturasieli:service_form'))

    context = {
        'client_services': client_services if client_services.exists() else None,
        'provider_services': provider_services if provider_services.exists() else None
    }
    return render(request, 'facturasieli/service/service.html', context)

# delete selected service
def delete_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    try:
        services = get_list_or_404(Service, company_client=request.profile.company) 
    except:
        return HttpResponseRedirect(reverse('facturasieli:service_form'))
    
    return render(request, 'facturasieli/service/service.html', {'services': services})
