# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/custom_log_in_view.py
# Author : Zineb
# ---------------------------------------------------------------------------

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import login

from facturasieli.models import Profile
from facturasieli.services.twoFA_service.create_otp import create_otp
from facturasieli.services.twoFA_service.send_otp_email import send_otp_mail
 ################# a enlever si otp remise
from facturasieli.services.inpi_authentification import INPIAuthClient
###################################""
from facturasieli.forms.CustomAuthenticationForm import CustomAuthenticationForm

def custom_log_in(request: HttpRequest):
    if request.method == 'GET':
        form = CustomAuthenticationForm()
        return render(request, 'registration/custom_login.html', {'form': form})
    
    form = CustomAuthenticationForm(request, data=request.POST)
    if not form.is_valid():
        messages.error(request, _('Invalid email or password.'))
        return render(request, 'registration/custom_login.html', {'form': form})

    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(request, username=username, password=password)
    ################# a enlever si otp remise
    login(request,user)
    if 'inpi_client' not in request.session:
            username = 'maurice.ambroise79@gmail.com'
            password = 'Morice300179!'
            client = INPIAuthClient(username,password)
            inpi_token = client.authenticate()
            request.session['inpi_client'] = inpi_token
    ################# 
    if user is None:
        messages.error(request,_('No user was found.'))
        return render(request, 'registration/custom_login.html', {'form': form})

    profile = get_object_or_404(Profile, email=username)
    otp_instance = create_otp(profile)
    send_otp_mail(otp_instance)
    request.session['pretended_user_id'] = user.id
    return HttpResponseRedirect(reverse('facturasieli:index'))
    #return HttpResponseRedirect(reverse('facturasieli:otp_validation'))

