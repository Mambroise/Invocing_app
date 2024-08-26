# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/send_email.py
# Author : Morice
# ---------------------------------------------------------------------------

import environ

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Notification,Profile

# initialise environment
env = environ.Env()
environ.Env.read_env(env_file='.env')

def send_email( notification : Notification,receiver_profile : Profile):
    # Sample notification data
    if notification.type == 10:
        object_content = _('New user recently registered:')
    else:
        object_text = _('New notification:')
        object_content = f"{receiver_profile.first_name}, {object_text} {notification.type}"

    notification_body = {
        'object': object_content,
        'title': notification.service_title,
        'notification_type': notification.type,
        'notification_date': notification.send_at,
        'notification_company_sender': notification.company_sender,
        'notification_company_siret': receiver_profile.company.siret,
        'user_profile' : receiver_profile
    }

    # Render the email template with context data
    subject = notification_body['object']
    from_email = env('EMAIL_HOST_USER')
    to_email = receiver_profile.email
    text_content = 'Your email client does not support HTML content'

    # In case of new_account
    if notification.type == 10:
        html_notification_content = render_to_string('facturasieli/email/registration_email.html', notification_body)
        html_new_user_content = render_to_string('facturasieli/email/new_user_email.html', notification_body)

        #email to the admin
        email2 = EmailMultiAlternatives(subject, text_content, from_email, [from_email])
        email2.attach_alternative(html_new_user_content, 'text/html')
        email2.send()
    else:
        html_notification_content = render_to_string('facturasieli/email/notification_email.html', notification_body)

    # Create the email message
    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_notification_content, 'text/html')

    # Send the email
    email.send()

def send_password_email(profile:Profile):

    # Render the email template with context data
    subject = _('Facturasieli: reset your password with this link')
    from_email = env('EMAIL_HOST_USER')
    to_email = profile.email
    text_content = 'Your email client does not support HTML content'

    html_reset_password_content = render_to_string('facturasieli/email/reset_password_email.html', {'user_profile':profile})

        # Create the email message
    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_reset_password_content, 'text/html')

    # Send the email
    email.send()
