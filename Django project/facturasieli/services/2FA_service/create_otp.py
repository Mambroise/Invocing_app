# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/service/2FA_service/create_otp.py
# Author : Morice
# ---------------------------------------------------------------------------

import secrets

from django.contrib.auth.models import User

from facturasieli.models import OTP

def create_otp(user : User):
    OTP.objects.filter(user=user).delete()
    new_otp = OTP(user=user,otp=secrets.token_urlsafe(4))
    print("OTPOTPOTPOTP= ",new_otp)
    new_otp.save()
    return new_otp