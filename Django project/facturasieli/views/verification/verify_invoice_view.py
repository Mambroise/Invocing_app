#<!---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/verify_invoice_view.py
# Author : Zineb
# -------------------------------------------------------------------------->

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from facturasieli.models import Invoice, Verification
from facturasieli.forms import VerificationForm



@login_required
#@user_passes_test(is_company_verifier_or_admin)
def verify_invoice_view(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)

    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            verification = form.save(commit=False)
            verification.invoice = invoice
            verification.verified_by = request.profile  
            verification.save()

            invoice.status = form.cleaned_data['status']
            invoice.save()
            messages.success = _('Invoice status updated successfully')
            pending_invoices = Invoice.objects.filter(status='Pending')  # 1 corresponds to 'Pending'
            return render(request, 'facturasieli/verification/verification_list.html', {'invoices': pending_invoices})
    else:
        form = VerificationForm()

    return render(request, 'facturasieli/verification/verification_form.html', {'invoice': invoice, 'form': form})
