# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/service/2FA_service/send_otp_email.py
# Author : Morice
# ---------------------------------------------------------------------------

import environ

from django.core.mail import EmailMultiAlternatives
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string

from facturasieli.models import OTP

# initialise environment
env = environ.Env()
environ.Env.read_env(env_file='.env')

def send_otp_mail(otp_instance: OTP):

    object_content: str = 'Easynvoice - ' + _('Authentication')
    salute: str = _('Hello')
    content: str = _('Your one time password: ')
    email_end: str = _('Please copy and paste these numbers in the app.')
    
    email_body = {
        'salute': salute,
        'content': content,
        'otp': otp_instance.otp,
        'email_end': email_end
    }

    subject: str =  object_content
    from_email: str =  env('EMAIL_HOST_USER')
    to_email = otp_instance.profile.email
    text_content = 'Your email client does not support HTML content'

    html_reset_password_content = render_to_string('facturasieli/email/otp_validation_email.html', email_body)

    # Create the email message
    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_reset_password_content, 'text/html')

    # Send the email
    email.send()
