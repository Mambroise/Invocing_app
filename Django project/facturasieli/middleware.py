# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/middleware.py
# Author : Team
# ---------------------------------------------------------------------------

from django.utils import timezone

from facturasieli.models import Profile


class ProfileMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile = Profile.objects.get(email=request.user)
            profile.last_request_timestamp = timezone.now()
            request.profile = profile
        else:
            request.profile = None

        response = self.get_response(request)
        return response
