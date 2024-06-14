# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/middleware.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from facturasieli.models import Profile,Notification

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


class notificationMiddleware:

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


class registrationCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.profile.company is None:
                registration_url = reverse('facturasieli:register2')
                logout_url = reverse('facturasieli:log_out')
                
                if request.path != registration_url and request.path != logout_url:
                    messages.error(request, _("You have to finish registration before logging in"))
                    return HttpResponseRedirect(registration_url)

        response = self.get_response(request)
        return response
