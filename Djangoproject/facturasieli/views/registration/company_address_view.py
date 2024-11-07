
# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/register_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpRequest,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from facturasieli.forms.CompanyForm import CompanyForm
from facturasieli.forms.AddressForm import AddressForm
from facturasieli.models import Profile
from facturasieli.services.notification_service import new_account

def register_company_address(request: HttpRequest):
    if request.method == 'POST':
        company_form =CompanyForm(request.POST)
        address_form =AddressForm(request.POST)
        if company_form.is_valid() and address_form.is_valid():
            try:
                profile = get_object_or_404(Profile, pk=request.profile.id)
                address =address_form.save()
                company = company_form.save(commit=False)
                
                company.address = address
                company.save()
                
                profile.company = company
                profile.save()

                # send welcome message in-app
                new_account(request,profile)
                messages.success(request, _("Thanks for subscribing. Let's get to work!"))
            except Exception as e:
                messages.error(request,_('subscribtion unsuccessful by encounturing issue: %s' % str(e)))
            
            return HttpResponseRedirect(reverse('facturasieli:index'))
    else:
        company_form = CompanyForm()
        address_form = AddressForm()

    context = {'company_form': company_form, 'address_form': address_form}
    return render(request, 'registration/register2.html', context)