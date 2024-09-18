# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/service/2FA_service/create_otp.py
# Author : Morice
# ---------------------------------------------------------------------------

import secrets

from facturasieli.models import OTP, Profile

def create_otp(profile : Profile):
    OTP.objects.filter(profile=profile).delete()
    
    new_otp_code = ''.join(str(secrets.randbelow(10)) for _ in range(6))
    
    new_otp = OTP(profile=profile, otp=new_otp_code)
    new_otp.save()
    
    return new_otp