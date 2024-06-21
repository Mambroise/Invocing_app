# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/invoice/invoice_view.py
# Author : Margaux,Morice
# ---------------------------------------------------------------------------


import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from facturasieli.forms.InvoiceForm import InvoiceForm
from facturasieli.models import Service,Invoice,NotificationType
from facturasieli.services.notification_service import send_notification

logger = logging.getLogger(__name__)

def invoice_view(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        form = InvoiceForm(request.POST)
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

            #sending notification in-app to the provider
            send_notification(notification_type= NotificationType.FACTURE_SOUMISE,
                            service_title= f"Facture pour l'intervention : {service.title}.",
                            company_sender_id= request.profile.company_id,
                            company_receiver_id=service.company_client.id
                            )

            messages.success(request, "Invoice saved successfully.")
            #redirect towards company services
    
            url = reverse('facturasieli:service', kwargs={'company_id': service.company_client.id})
            return redirect(url)
        else:
            logger.error("Form is not valid: %s", form.errors)
            messages.error(request, "There were errors in your form. Please correct them and try again.")
    else:
        form = InvoiceForm()
    
    return render(request, 'facturasieli/invoice/invoice_form.html', {'form': form, 'service': service})

