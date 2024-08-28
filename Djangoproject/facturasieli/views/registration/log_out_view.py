# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/log_out_view.py
# Author : Brice
# ---------------------------------------------------------------------------

from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def log_out(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    if request.method == 'POST':
        logout(request)
        messages.success(request,_('You have been successfully logged out. We hope to see you again soon!'))
        return HttpResponseRedirect(reverse('facturasieli:index'))
    return render(request, 'registration/logout.html')
