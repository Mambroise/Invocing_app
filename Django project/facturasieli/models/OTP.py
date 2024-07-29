from django.conf import settings
from django.db import models
from facturasieli.models.utils import compute_expiration_timestamp
from facturasieli.models import Profile

class OTP(models.Model):
    profile = models.OneToOneField('facturasieli.Profile', on_delete=models.CASCADE)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    expiration_timestamp = models.DateTimeField(default=compute_expiration_timestamp)
    otp = models.CharField(max_length=10)

