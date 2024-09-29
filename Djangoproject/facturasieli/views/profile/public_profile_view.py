# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/profile/public_profile_view.py
# Author : Brice
# ---------------------------------------------------------------------------

from django.db.models import Q
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Service,Invoice,Role


def public_profile(request: HttpRequest, user_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    # gathering all user informations
    profile = request.profile
    company = profile.company

    # provider part
    services_nbr = Service.objects.filter(company_provider=company.id).count()
    pending_invoice_nbr = Invoice.objects.filter(name_provider=company.name, status=1).count()
    accepted_invoice_nbr = Invoice.objects.filter(name_provider=company.name, status=2).count()

    # client part
    client_services_nbr = Service.objects.filter(
        Q(company_client=company.id) & 
        (Q(status='Invoice Request Sent') | Q(status='Demande de facture envoyée'))
    ).count()
    # Q Objects : Les objets Q permettent de créer des expressions complexes dans les requêtes Django.
    # Ils sont particulièrement utiles pour combiner des conditions avec des opérateurs logiques comme OR.
    paid_invoice_nbr = Invoice.objects.filter(name_provider=company.name, status=4).count()

    try:
        invoice_to_pay = Invoice.objects.filter(name_client=company.name, status=2)
    except:
        invoice_to_pay=[]

    context = {"profile":profile, "company":company,
                "services_nbr":services_nbr,
                "pending_invoice_nbr":pending_invoice_nbr,
                "accepted_invoice_nbr":accepted_invoice_nbr,
                "paid_invoice_nbr":paid_invoice_nbr,
                "client_services_nbr":client_services_nbr,
                "invoice_to_pay":invoice_to_pay
                }
    return render(request, 'facturasieli/profile/public_profile.html',context)
