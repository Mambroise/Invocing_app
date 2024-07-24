# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/send_email.py
# Author : Morice
# ---------------------------------------------------------------------------

import environ
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from facturasieli.models import Notification,Profile

# initialise environment
env = environ.Env()
environ.Env.read_env(env_file='.env')

def send_email(request, notification : Notification,receiver_profile : Profile):
    # Sample notification data
    
    notification_body = {
        'object': f"{receiver_profile.first_name} {notification.service_title}",
        'title': notification.service_title,
        'notification_type': notification.type,
        'notification_date': notification.send_at,
        'notification_company_sender': notification.company_sender,
        'notification_company_siret': receiver_profile.company.siret,
        'username' : receiver_profile.first_name
    }

    # Render the email template with context data
    subject = notification_body['object']
    from_email = env('EMAIL_HOST_USER')
    to_email = receiver_profile.email
    html_content = render_to_string('facturasieli/email/notification_email.html', notification_body)
    text_content = 'Your email client does not support HTML content'

    # Create the email message
    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, 'text/html')

    # Send the email
    email.send()
