# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/profile/edit_password.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages 

from facturasieli.forms import ResetPasswordForm,EmailCheckForm
from facturasieli.models import Profile
from facturasieli.services.send_email import send_password_email

def account_check(request):
    
    if request.method == 'POST':
        form = EmailCheckForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            try:
                profile = Profile.objects.get(email=email)
                
                send_password_email(profile)
                messages.success(request, 'An email has been sent to reset your password.')
                return HttpResponseRedirect(reverse('facturasieli:index'))
            
            except Profile.DoesNotExist:
                # Si l'utilisateur n'existe pas, afficher un message d'erreur
                messages.error(request, 'No account found with this email address.')
                return HttpResponseRedirect(reverse('facturasieli:account_check'))
        else:
            messages.error(request, 'Invalid email address')
            return HttpResponseRedirect(reverse('facturasieli:account_check'))
    
    form = EmailCheckForm()

    context = { 'form': form }
    return render(request, 'facturasieli/profile/account_check.html', context)

def reset_password(request, profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id)
    except Profile.DoesNotExist:
        messages.error(request, 'Profile not found.')
        return HttpResponseRedirect(reverse('facturasieli:index'))

    if request.method == 'POST':
        form = ResetPasswordForm(request,request.POST)
        if form.is_valid():
            new_pwd = form.cleaned_data['password1']
            profile.set_password(new_pwd)
            profile.save()
            messages.success(request, 'Password successfully updated.')
            return HttpResponseRedirect(reverse('facturasieli:index'))
    else:
        form = ResetPasswordForm(request)

    context = { 'form': form, 'profile': profile }
    return render(request, 'facturasieli/profile/reset_password.html', context)
