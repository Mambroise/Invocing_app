from django.conf import settings
from django.db import models
from facturasieli.models.utils import compute_expiration_timestamp

class OTP(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    expiration_timestamp = models.DateTimeField(default=compute_expiration_timestamp)
    otp = models.CharField(max_length=10)

    def __str__(self):
        return self.user.email  # Assuming the email is the unique identifier for your custom user model
