# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/profile/edit_company_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from facturasieli.forms.CompanyForm import CompanyForm
from facturasieli.forms.AddressForm import AddressForm


def edit_company(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    company = request.profile.company
    address = company.address
    
    if request.method == 'POST':
        company_form = CompanyForm(request.POST, instance=company)
        address_form = AddressForm(request.POST, instance=address)
        
        if company_form.is_valid() and address_form.is_valid():
            company_form.save()
            address_form.save()
            url = reverse('facturasieli:public_profile', kwargs={'user_id': request.profile.id})
            return HttpResponseRedirect(url)
    else:
        company_form = CompanyForm(instance=company)
        address_form = AddressForm(instance=address)
    
    context = { 'company_form': company_form, 'address_form': address_form }
    return render(request, 'facturasieli/profile/edit_company.html', context)
