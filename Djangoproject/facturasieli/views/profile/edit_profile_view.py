# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/profile/edit_profile_view.py
# Author : Brice
# ---------------------------------------------------------------------------

import os

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.forms import EditProfileForm
from facturasieli.models import Profile

def edit_profile(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    profile = request.profile
    old_avatar = profile.avatar.path

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False) 
            if request.FILES:
                if not 'default_avatar' in old_avatar:
                    try:
                        os.remove(old_avatar)
                    except:
                        pass
            profile.save() 
            request.user.email = request.POST.get('email', '')
            request.user.save() 

            url = reverse('facturasieli:public_profile', kwargs={ 'user_id': request.profile.id })
            return redirect(url)
        else:
            print(form.errors)
    else:
        form = EditProfileForm(initial={'email': request.user.email}, instance=profile)

    context = {'form': form}
    return render(request, 'facturasieli/profile/edit_profile.html', context)




