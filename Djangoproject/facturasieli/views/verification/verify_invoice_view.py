#<!---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/verify_invoice_view.py
# Author : Zineb,Morice
# -------------------------------------------------------------------------->

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _
from facturasieli.models import Invoice, Service
from facturasieli.forms import VerificationForm
from facturasieli.services.notification_service import invoice_verified, invoice_rejected
from facturasieli.services.all_maths import invoice_total_amount



@login_required
#@user_passes_test(is_company_verifier_or_admin)
def verify_invoice_view(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    service = get_object_or_404(Service, invoice=invoice)

    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            verification = form.save(commit=False)
            verification.invoice = invoice
            verification.verified_by = request.profile  
            verification.save()

            invoice_status = form.cleaned_data['status']
            invoice.status = invoice_status
            invoice.save()

            #sending notification in-app to the provider
            if invoice_status == "2":
                invoice_verified(request,service)
            else:
                invoice_rejected(request, service)


            # select invoices according to the user role
            if request.profile.has_role(['Company manager','Company Verifier']):
                pending_invoices = Invoice.objects.filter(status=1,name_client=request.profile.company.name) 
            elif request.profile.has_role(['Admin']):
                pending_invoices = Invoice.objects.filter(status=1)
            else:
                pending_invoices = None

            messages.success = _('Invoice status updated successfully')
            pending_invoices = Invoice.objects.filter(status=1)  # 1 corresponds to 'Pending'
            return render(request, 'facturasieli/verification/verification_list.html', {'invoices': pending_invoices})
    else:
 
        total_price = invoice_total_amount(invoice)
        form = VerificationForm()

        context = {'invoice': invoice, 'form': form, 'total': total_price}

    return render(request, 'facturasieli/verification/verification_form.html', context )
