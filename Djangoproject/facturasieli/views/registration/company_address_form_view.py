
# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/company_address_form_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpRequest
from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from facturasieli.forms.CompanyForm import CompanyForm
from facturasieli.forms.AddressForm import AddressForm
from facturasieli.models import Company, Address


def company_address_form(request: HttpRequest):
    if request.method == 'POST':
        siret = request.POST.get('siret')
        name = request.POST.get('name')
        activity = request.POST.get('activity')
        description = request.POST.get('description')
        number = request.POST.get('number')
        street = request.POST.get('street')
        zip_code = request.POST.get('zip_code')
        city = request.POST.get('city')
        country = request.POST.get('country')

        address = Address(
            number=number,
            street=street,
            zip_code=zip_code,
            city=city,
            country=country
        )

        company = Company(
            siret=siret,
            name=name,
            activity=activity,
            description=description,
            address =address
        )
    
        company_form = CompanyForm(instance=company)
        address_form = AddressForm(instance=address)

        context = {'company_form': company_form, 'address_form': address_form}
        return render(request, 'registration/register2.html', context)