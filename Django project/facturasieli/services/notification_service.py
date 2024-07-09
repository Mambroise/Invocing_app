# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/notification_service.py
# Author : Arnaud
# ---------------------------------------------------------------------------

from datetime import datetime

from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Company,Notification,NotificationType,Service

# all notification messages
invoice_submitted_message = _("Invoice for service:")
invoice_updated_message = _("Invoice modified for service:")
invoice_deleted_message = _("Invoice deleted for service:")

# MAIN FUNCTION, saving in database function
@staticmethod
def send_notification(notification_type:str, service_title:str, company_sender_id:int, company_receiver_id:int):
    company_sender = get_object_or_404(Company, pk=company_sender_id)
    company_receiver = get_object_or_404(Company, pk=company_receiver_id)

    notification = Notification()
    notification.send_at = datetime.now()
    notification.type=notification_type
    notification.service_title = service_title
    notification.company_sender = company_sender
    notification.company_receiver = company_receiver
    notification.save()

#sending notification in-app to the client after creating the invoice
def invoice_submitted(request, service : Service):

    send_notification(notification_type= NotificationType.INVOICE_SUBMITTED,
                service_title= f"{invoice_deleted_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_client.id
                )
    
#sending notification in-app to the client after updating the invoice
def invoice_updated(request, service : Service):

    send_notification(notification_type= NotificationType.INVOICE_MODIFIED,
                service_title= f"{invoice_updated_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_client.id
                )
    
#sending notification in-app to the client after updating the invoice
def invoice_deleted(request, service : Service):

    send_notification(notification_type= NotificationType.INVOICE_DELETED,
                service_title= f"{invoice_updated_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_client.id
                )
