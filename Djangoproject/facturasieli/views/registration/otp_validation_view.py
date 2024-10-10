
# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/otp_validation_view.py
# Author : Brice
# ---------------------------------------------------------------------------

import environ
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from facturasieli.forms.OTPForm import OTPForm
from facturasieli.models import OTP
from facturasieli.services.inpi_authentification import INPIAuthClient

# initialise environment
env = environ.Env()
environ.Env.read_env(env_file='.env')

def otp_validation(request: HttpRequest):
    if request.method == 'GET':
        form = OTPForm()
        return render(request, 'registration/otp_validation.html', {'form': form})

    form = OTPForm(request.POST)
    if not form.is_valid():
        return render(request, 'registration/otp_validation.html', {'form': form})

    user_otp = form.cleaned_data['otp']
    pretended_user_id = request.session.get('pretended_user_id', '')
    if not pretended_user_id:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    otp_instance = OTP.objects.filter(
        otp=user_otp,
        profile=pretended_user_id).first()
    if otp_instance:
        if otp_instance.expiration_timestamp > timezone.now():
            login(request, otp_instance.profile)
            if 'inpi_client' not in request.session:
                username = env('INPI_USERNAME')
                password = env('INPI_PASSWORD')
                client = INPIAuthClient(username,password)
                inpi_token = client .authenticate()
                request.session['inpi_client'] = inpi_token
            return HttpResponseRedirect(reverse('facturasieli:index'))
        else:
            messages.error(request,_('Time to sign in is out, please retry'))
            return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    else:
        messages.error(request,_('Your one time password is not valid'))
    return render(request, 'registration/otp_validation.html', {'form': form})
