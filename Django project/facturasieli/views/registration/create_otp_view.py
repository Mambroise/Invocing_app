# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/create_otp_view.py
# Author : Brice
# ---------------------------------------------------------------------------

import secrets

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from facturasieli.models import OTP


def create_otp(user: User):
    OTP.objects.filter(user=user.id).delete()
    new_otp = OTP(user=user, otp=secrets.token_urlsafe(4))
    new_otp.save()
    return new_otp
