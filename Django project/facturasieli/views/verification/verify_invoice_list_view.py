# facturasieli/views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from facturasieli.models import Invoice, Verification, Role, Profile
from facturasieli.forms import VerificationForm

# Vérifiez si l'utilisateur a le rôle 'admin' ou 'Company Verifier'
def is_company_verifier_or_admin(user):
    profile = Profile.objects.get(email=user.email)
    return profile.role.filter(role__in=['admin', 'Company Verifier']).exists()

@login_required
#@user_passes_test(is_company_verifier_or_admin)
def verify_invoice_list_view(request):
    pending_invoices = Invoice.objects.filter(status='Pending')  # 1 corresponds to 'Pending'
    return render(request, 'facturasieli/verification/verification_list.html', {'invoices': pending_invoices})
