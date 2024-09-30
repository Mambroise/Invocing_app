# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/profile/edit_profile_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from facturasieli.forms import EditProfileForm,ResetPasswordForm
from facturasieli.services.notification_service import account_modified

def edit_profile(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    profile = request.profile

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile, user = request.user)
        if form.is_valid():
            try:
                request.user.last_name = request.POST.get('last_name', '')
                request.user.first_name = request.POST.get('first_name', '')
                request.user.email = request.POST.get('email', '')
                request.user.save() 

                messages.success(request, _('Your profile has successfully been updated'))

                # sending email and notification to notif change
                account_modified(request, request.profile)
            except:
                messages.error(request, _('Your profile upadte has failed, please try again'))


            url = reverse('facturasieli:public_profile', kwargs={ 'user_id': request.profile.id })
            return redirect(url)
        else:
            print(form.errors)
    else:
        form = EditProfileForm(initial={'email': request.user.email}, instance=profile, user = request.user)

    context = {'form': form}
    return render(request, 'facturasieli/profile/edit_profile.html', context)


def change_password(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    if request.method == 'POST':
        form = ResetPasswordForm(request,request.POST)
        if form.is_valid():
            profile = request.profile
            new_pwd = form.cleaned_data.get('password1')
            profile.set_password(new_pwd)
            profile.save()

            messages.success(request, _('Your password has successfully been updated'))

            url = reverse('facturasieli:edit_profile')
            return redirect(url)
        else:
            messages.error(request, _('Your password upadte has failed, please try again'))

    form = ResetPasswordForm(request)
    context = {'form': form}

    return render(request, 'facturasieli/profile/reset_password.html', context)