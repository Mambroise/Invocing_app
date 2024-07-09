# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/show_service_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Service
from facturasieli.services.all_maths import invoice_total_amount


def show_service(request, service_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    service = get_object_or_404(Service, id = service_id)

    total_price = invoice_total_amount(service.invoice)

    context = {'service':service, 'total':total_price}
    return render(request, 'facturasieli/service/show_service.html', context)
