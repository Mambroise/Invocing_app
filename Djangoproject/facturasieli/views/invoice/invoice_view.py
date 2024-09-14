# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/invoice/invoice_view.py
# Author : Margaux,Morice
# ---------------------------------------------------------------------------


import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from facturasieli.forms.InvoiceForm import InvoiceForm
from facturasieli.models import Service,Invoice
from facturasieli.services.notification_service import invoice_submitted,invoice_updated,invoice_deleted
from facturasieli.services.generate_PDF import generate_pdf_invoice

logger = logging.getLogger(__name__)

def invoice_view(request, service_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.service = service
            invoice.name_provider = service.company_provider.name
            invoice.name_client = service.company_client.name
            invoice.client_address = service.company_client.address
            invoice.provider_address = service.company_provider.address
            invoice.save()

            # generation of unique invoice number
            invoice_id= invoice.id
            today_str = timezone.now().strftime('%Y%m%d')
            invoice_number = f"{invoice_id}{request.profile.company_id}{today_str}"
            invoice.invoice_number = invoice_number
            invoice.save()

            # service update with the new invoice id.
            service.invoice = get_object_or_404(Invoice, pk=invoice_id) 
            service.save()

            #sending notification in-app to the client
            invoice_submitted(request,service)

            messages.success(request, _("Invoice saved successfully."))
            #redirect towards company services
    
            url = reverse('facturasieli:show_service', kwargs={'service_id': service.id})
            return redirect(url)
        else:
            logger.error("Form is not valid: %s", form.errors)
            messages.error(request, _("There were errors in your form. Please correct them and try again."))
    else:
        form = InvoiceForm()
    
    return render(request, 'facturasieli/invoice/invoice_form.html', {'form': form, 'service': service})


def update_invoice(request, service_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    service = get_object_or_404(Service, pk=service_id)
    invoice = service.invoice

    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES, instance=invoice)
        if form.is_valid():
            updated_invoice = form.save(commit=False)
            
            # Ensure required fields are set (re-assign existing values to unchanged fields)
            updated_invoice.invoice_number = invoice.invoice_number
            updated_invoice.client_address = invoice.client_address
            updated_invoice.provider_address = invoice.provider_address
            updated_invoice.name_provider = invoice.name_provider
            updated_invoice.name_client = invoice.name_client
            updated_invoice.update_timestamp = timezone.now()
            updated_invoice.attachment = invoice.attachment


            updated_invoice.save()
            messages.success(request,_("Invoice successfully updated."))
           
            #sending notification in-app to the client
            invoice_updated(request,service)

            url = reverse('facturasieli:show_service', kwargs={'service_id': service.id})
            return redirect(url)
        else:
            logger.error('Form is not valid:%s',form.errors)
            messages.error(request, _("There were errors in your form. Please correct them and try again."))

    form = InvoiceForm(instance=invoice)

    return render(request,'facturasieli/invoice/invoice_form.html',{'form':form, 'service':service} )


def delete_invoice(request, service_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    service = get_object_or_404(Service, pk=service_id)
    invoice = service.invoice
    invoice.delete()

    #get service after invoice deletion
    service = get_object_or_404(Service, pk=service_id)

    #sending notification in-app to the client
    invoice_deleted(request, service)

    return render(request, 'facturasieli/service/show_service.html', {'service': service})

def print_invoice(request, invoice_id):
    return generate_pdf_invoice(request, invoice_id, method='inline')
