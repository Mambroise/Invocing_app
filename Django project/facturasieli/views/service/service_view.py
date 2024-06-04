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

# display the user service list
def display_service(request, company_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    try:
        services = get_list_or_404(Service, company_client=company_id)
    except:
        return HttpResponseRedirect(reverse('facturasieli:service_form'))

    return render(request, 'facturasieli/service/service.html', {'services': services})

# delete selected service
def delete_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    services = get_list_or_404(Service, company_client=request.profile.company)
    return render(request, 'facturasieli/service/service.html', {'services': services})
