# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/service_form_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from facturasieli.forms import ServiceForm
from facturasieli.models import Company, NotificationType, Service
from facturasieli.services.notification_service import send_notification


def handle_service(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            try:
                service_data = form.cleaned_data
                
                #get the companies envolved
                company_provider = get_object_or_404(Company, pk=service_data['company_provider'].id)
                company_client = get_object_or_404(Company, pk=request.profile.company_id)

                # create the service object
                new_service = Service(
                    title=service_data['title'],
                    description=service_data['description'],
                    issue_date=timezone.now(),
                    intervention_start_date=service_data['intervention_start_date'],
                    intervention_end_date=service_data['intervention_end_date'],
                    company_provider=company_provider,
                    company_client=company_client
                )
                new_service.save()
                
                #sending notification in-app to the provider
                send_notification(notification_type= NotificationType.DEMANDE_FACTURE,
                                service_title= f"Demande de facture pour l'intervention : {new_service.title}.",
                                company_sender_id= request.profile.company_id,
                                company_receiver_id=new_service.company_provider.id
                                )
                
                messages.success(request, _("Service created successfully."))
                
                url = reverse('facturasieli:service', kwargs={'company_id': request.profile.company_id})
                return redirect(url) 
            except Exception as e:
                messages.error(request, _("An error occurred while saving the service: %s" % str(e)))
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = ServiceForm()

    return render(request, 'facturasieli/service/service_form.html', {"form": form})
