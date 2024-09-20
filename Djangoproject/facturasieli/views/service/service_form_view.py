# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/service_form_view.py
# Author : Morice
# ---------------------------------------------------------------------------

import logging
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from facturasieli.forms import ServiceForm
from facturasieli.models import Company,Service
from facturasieli.services.notification_service import invoice_request,service_updated

logger = logging.getLogger(__name__)

def handle_service(request, company_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    #selected company
    company_provider = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            try:
                service_data = form.cleaned_data
                
                #get the user company
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
                try:
                    invoice_request(request, new_service)
                    messages.success(request, _("Service created successfully."))
                except Exception as e:
                    messages.warning(request,_('Service successfully created but we may encountured issues: %s' % str(e)))
                
                
                url = reverse('facturasieli:service')
                return redirect(url) 
            except Exception as e:
                messages.error(request, _("An error occurred while saving the service: %s" % str(e)))
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = ServiceForm()
    context = {"form": form, "company_provider":company_provider}
    return render(request, 'facturasieli/service/service_form.html', context)

def update_service(request, service_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    service = get_object_or_404(Service, pk=service_id)
    service = get_object_or_404(Service, pk=service_id)
    previous_title = service.title
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            update_service = form.save(commit=False)
            client_company = get_object_or_404(Company,pk=request.profile.company_id)

            update_service.issue_date = service.issue_date
            update_service.status = service.status
            update_service.company_client = client_company
            update_service.save()

            #sending notification in-app to the provider
            service_updated(request,update_service)

            #sending notification in-app to the provider
            invoice_request(request, update_service)
            
            messages.success(request, _('Service successfully updated.'))

            url = reverse('facturasieli:show_service', kwargs={'service_id':service.id})
            return redirect(url)
        else:
            logger.error('Form is valid:%s',form.errors)
            messages.error(request, _("There were errors in your form. Please correct them and try again."))


    form = ServiceForm(instance=service)

    return render(request, 'facturasieli/service/service_form.html', {"form":form, 'update':'update_mode'})
