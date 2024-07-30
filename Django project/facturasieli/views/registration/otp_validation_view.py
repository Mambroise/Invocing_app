
# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/otp_validation_view.py
# Author : Brice
# ---------------------------------------------------------------------------

from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from facturasieli.forms import OTPForm
from facturasieli.models import OTP


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
            return HttpResponseRedirect(reverse('facturasieli:index'))
        else:
            messages.error(request,_('Time to sign in is out, please retry'))
            return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))

    return render(request, 'registration/otp_validation.html', {'form': form})
