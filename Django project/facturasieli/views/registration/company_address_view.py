# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/register_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpRequest,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from facturasieli.forms.CompanyForm import CompanyForm
from facturasieli.forms.AddressForm import AddressForm

def register_company_address(request: HttpRequest):
    if request.method == 'POST':
        company_form =CompanyForm(request.POST)
        address_form =AddressForm(request.POST)
        if company_form.is_valid() and address_form.is_valid():
            address =address_form.save()
            company = company_form.save(commit=False)
            company.address = address
            company.save()
            return HttpResponseRedirect(reverse('facturasieli:welcome'))
    else:
        company_form = CompanyForm()
        address_form = AddressForm()

    context = {'company_form': company_form, 'address_form': address_form}
    return render(request, 'registration/register2.html', context)