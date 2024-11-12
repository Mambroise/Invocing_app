# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/middleware.py
# Author : Morice
# ---------------------------------------------------------------------------

import datetime
import pytz
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.conf import settings

from facturasieli.models import Profile,Notification,Invoice

class ProfileMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(email=request.user.email)
                profile.last_request_timestamp = timezone.now()
                profile.save()
                request.profile = profile
            except Profile.DoesNotExist:
                request.profile = None
        else:
            request.profile = None

        response = self.get_response(request)
        return response


class NotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:
            try:
                notifications_to_read = Notification.objects.filter(company_receiver=request.profile.company, is_read=False).count()
                request.notifications_to_read = notifications_to_read
            except Notification.DoesNotExist:
                request.notifications_to_read=None

        response = self.get_response(request)
        return response

class RegistrationCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.profile.company is None:
                logout_url = reverse('facturasieli:log_out')
                registration_url = reverse('facturasieli:register2')
                company_register_url = reverse('facturasieli:register3')
                company_register2_url = reverse('facturasieli:register4')
                
                if request.path != registration_url and request.path != logout_url and request.path != company_register_url and request.path != company_register2_url:
                    print(request.path)
                    messages.error(request, _("You have to finish registration before logging in"))
                    return HttpResponseRedirect(registration_url)

        response = self.get_response(request)
        return response

class InactivityLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)
        
        now = timezone.now()
        last_activity = request.session.get('last_activity')

        if last_activity:
            last_activity = datetime.datetime.fromisoformat(last_activity).replace(tzinfo=pytz.UTC)
            if now - last_activity > datetime.timedelta(minutes=settings.INACTIVITY_TIMEOUT_MINUTES):
                messages.error(request, _('You have been logged out due to inactivity.'))
                logout(request)
                return self.get_response(request)
        
        request.session['last_activity'] = now.isoformat()
        return self.get_response(request)