# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/service_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Service
from facturasieli.services.notification_service import service_deleted


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
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    service = get_object_or_404(Service, pk=service_id)
    service.delete()

    #sending notification in-app to the provider
    try:
        service_deleted(request, service)
        messages.success(request,_('Service successfully deleted'))
    except Exception as e:
        messages.warning(request,_('Service successfully deleted but we may had issues sending emails: %s' % str(e)))
    
    company_id = request.profile.company.id
    client_services = Service.objects.filter(company_client=company_id)
    provider_services = Service.objects.filter(company_provider=company_id)

    context = {
        'client_services': client_services if client_services.exists() else None,
        'provider_services': provider_services if provider_services.exists() else None
    }
    
    return render(request, 'facturasieli/service/service.html', context)
