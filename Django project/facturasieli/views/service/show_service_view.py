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


def show_service(request, service_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    service = get_object_or_404(Service, id = service_id)

    # Total price math
    try:
        if service.invoice.tax == 1:
            vat = 20
        elif service.invoice.tax == 2:
            vat = 10
        elif service.invoice.tax == 4:
            vat = 5.5
        elif service.invoice.tax == 5:
            vat = 2.1
        total_price = service.invoice.amount_excluding_tax + (service.invoice.amount_excluding_tax * (vat / 100))
    except:
        total_price = 0

    context = {'service':service, 'total':total_price}
    return render(request, 'facturasieli/service/show_service.html', context)
