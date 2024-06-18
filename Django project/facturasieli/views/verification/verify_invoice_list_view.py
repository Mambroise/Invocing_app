# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/invoice/verify_invoice_list_view.py
# Author : Morice
# ---------------------------------------------------------------------------

# facturasieli/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from facturasieli.models import Invoice, Profile

@login_required
#@user_passes_test(is_company_verifier_or_admin)
def verify_invoice_list_view(request):
    profile = Profile.objects.get(email=request.user.email)
    # select invoices according to the user role
    if profile.has_role(['Company manager','Company Verifier']):
        pending_invoices = Invoice.objects.filter(status=1,name_client=profile.company.name)  # 1 corresponds to 'Pending'
    elif profile.has_role(['Admin']):
        pending_invoices = Invoice.objects.filter(status=1)
    else:
        pending_invoices = None

    return render(request, 'facturasieli/verification/verification_list.html', {'invoices': pending_invoices})
