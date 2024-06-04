# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/profile/public_profile_view.py
# Author : Brice
# ---------------------------------------------------------------------------

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Profile


def public_profile(request: HttpRequest, user_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    user_to_show = get_object_or_404(User, pk=user_id)
    profile_to_show = get_object_or_404(Profile, email=user_to_show)

    context = {
        'profile': profile_to_show,
    }
    return render(request, 'facturasieli/public_profile.html', context)
