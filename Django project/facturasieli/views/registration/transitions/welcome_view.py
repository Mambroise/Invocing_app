# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/transitions/welcome_view.py
# Author : Brice
# ---------------------------------------------------------------------------

from django.http import HttpRequest
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def welcome(request: HttpRequest):
    return render(request, 'registration/transitions/welcome.html')
