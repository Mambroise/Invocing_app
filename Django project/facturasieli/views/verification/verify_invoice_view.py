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
from facturasieli.models import Invoice, NotificationType, Company
from facturasieli.forms import VerificationForm
from facturasieli.services.notification_service import send_notification



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

            invoice_status = form.cleaned_data['status']
            print(invoice_status)
            invoice.status = invoice_status
            invoice.save()

            #sending notification in-app to the provider
            provider_company = get_object_or_404(Company, name=invoice.name_provider)
            if invoice_status == "2":
                NotificationType_enum = NotificationType.FACTURE_VERIFIEE
            else:
                NotificationType_enum = NotificationType.FACTURE_REJETEE

            send_notification(notification_type= NotificationType_enum,
                            service_title= f"Facture pour la facture : {invoice.invoice_number}.",
                            company_sender_id= request.profile.company_id,
                            company_receiver_id=provider_company.id
                            )

            messages.success = _('Invoice status updated successfully')
            pending_invoices = Invoice.objects.filter(status='Pending')  # 1 corresponds to 'Pending'
            return render(request, 'facturasieli/verification/verification_list.html', {'invoices': pending_invoices})
    else:
                # Total price math
        try:
            total_price = invoice.amount_excluding_tax * (1 + invoice.tax / 100)
        except:
            total_price=0
        form = VerificationForm()

        context = {'invoice': invoice, 'form': form, 'total': total_price}

    return render(request, 'facturasieli/verification/verification_form.html', context )
