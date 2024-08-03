# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/profile/public_profile_view.py
# Author : Brice
# ---------------------------------------------------------------------------

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Profile,Service,Invoice


def public_profile(request: HttpRequest, user_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    # gathering all user informations
    profile = request.profile
    company = profile.company

    services_nbr = Service.objects.filter(company_provider=company.id).count()
    pending_invoice_nbr = Invoice.objects.filter(name_provider=company.name, status=1).count()
    accepted_invoice_nbr = Invoice.objects.filter(name_provider=company.name, status=2).count()
    paid_invoice_nbr = Invoice.objects.filter(name_provider=company.name, status=4).count()

    context = {"profile":profile, "company":company,
                "services_nbr":services_nbr,
                "pending_invoice_nbr":pending_invoice_nbr,
                "accepted_invoice_nbr":accepted_invoice_nbr,
                "paid_invoice_nbr":paid_invoice_nbr
                }
    return render(request, 'facturasieli/profile/public_profile.html',context)
