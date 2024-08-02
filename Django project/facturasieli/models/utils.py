# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/utils.py
# Author : Brice,Morice
# ---------------------------------------------------------------------------
import environ
from datetime import timedelta

from django.utils import timezone
from django.conf import settings


# initialise environment
env = environ.Env()
environ.Env.read_env(env_file='.env')

def get_avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/avatar
    return 'user_{0}/avatar'.format(instance.user.id)


def compute_expiration_timestamp():
    return timezone.now() + timedelta(seconds=settings.OTP_VALIDITY_DURATION)
