# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/custom_log_in_view.py
# Author : Zineb
# ---------------------------------------------------------------------------

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Profile
from facturasieli.services.twoFA_service.create_otp import create_otp
from facturasieli.services.twoFA_service.send_otp_email import send_otp_mail


def custom_log_in(request: HttpRequest):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'registration/custom_login.html', {'form': form})
    
    form = AuthenticationForm(request, data=request.POST)
    if not form.is_valid():
        return render(request, 'registration/custom_login.html', {'form': form})

    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(request, username=username, password=password)
    
    if user is None:
        return render(request, 'registration/custom_login.html', {'form': form})

    profile = get_object_or_404(Profile, email=username)
    otp_instance = create_otp(profile)
    send_otp_mail(otp_instance)
    request.session['pretended_user_id'] = user.id
    return HttpResponseRedirect(reverse('facturasieli:otp_validation'))

