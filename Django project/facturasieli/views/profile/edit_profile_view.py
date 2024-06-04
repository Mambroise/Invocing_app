# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/profile/edit_profile_view.py
# Author : Brice
# ---------------------------------------------------------------------------

import os

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.forms import ProfileForm


def edit_profile(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    old_avatar = request.profile.avatar.path

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.profile)
        if form.is_valid():
            if request.FILES:
                if not 'default_avatar' in old_avatar:
                    try:
                        os.remove(old_avatar)
                    except:
                        pass
            form.save()

            request.user.email = request.POST.get('email', '')
            request.user.save()

            return HttpResponseRedirect(reverse('facturasieli:index'))
    else:
        form = ProfileForm(
            initial={'email': request.user.email},
            instance=request.profile
        )

    context = { 'form': form }
    return render(request, 'facturasieli/edit_profile.html', context)



