# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/show_service_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Service, Invoice
from facturasieli.forms.InvoiceAttachmentForm import InvoiceAttachmentForm
from facturasieli.services.all_maths import invoice_total_amount

def show_service(request, service_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    #get the concerned service and invoice
    service = get_object_or_404(Service, id=service_id)
    invoice = service.invoice 

    total_price = invoice_total_amount(invoice) if invoice else 0

    #add the BIS attachment form
    if request.method == 'POST':
        form = InvoiceAttachmentForm(request.POST, request.FILES, instance=invoice)
        if form.is_valid():
            form.save()

            return redirect('facturasieli:show_service', service_id=service_id)
    else:
        form = InvoiceAttachmentForm(instance=invoice)

    context = {
        'service': service,
        'total': total_price,
        'form': form,
    }
    return render(request, 'facturasieli/service/show_service.html', context)
