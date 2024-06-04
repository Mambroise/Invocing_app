# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/index/index_view.py
# Author : Brice
# ---------------------------------------------------------------------------

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def index(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    context = {}
    return render(request, 'facturasieli/index.html', context)
