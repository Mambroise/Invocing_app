# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/middleware.py
# Author : Team
# ---------------------------------------------------------------------------

from typing import Any
from django.utils import timezone
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