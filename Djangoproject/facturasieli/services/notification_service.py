# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/notification_service.py
# Author : Morice
# ---------------------------------------------------------------------------

from datetime import datetime

from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Company,Notification,NotificationType,Service,Profile
from facturasieli.services.send_email import send_email

# all notification messages
Welcome_message = _('Thank you for registering and welcome to your new invoicing app')
account_modified_message = _('Account successfully updated')
invoice_submitted_message = _("Invoice submitted for service:")
invoice_updated_message = _("Invoice modified for service:")
invoice_deleted_message = _("Invoice deleted for service:")
invoice_request_message = _("Invoice request for service:")
invoice_verified_message = _("Invoice accepted and ready to be paid for service:")
invoice_paid_message = _("Invoice paid for service:")
invoice_rejected_message = _("Invoice rejected, check the file for service:")
service_updated_message = _("Modification of service:")
service_deleted_message = _("Deletion of service:")

#----------------------------------------------------
# MAIN FUNCTION, saving in database function
#----------------------------------------------------
@staticmethod
def send_notification(request,notification_type:str, service_title:str, company_sender_id:int, company_receiver_id:int):
    company_sender = get_object_or_404(Company, pk=company_sender_id)
    company_receiver = get_object_or_404(Company, pk=company_receiver_id)
    receiver_profile = get_object_or_404(Profile, company = company_receiver)

    notification = Notification()
    notification.send_at = datetime.now()
    notification.type=notification_type
    notification.service_title = service_title
    notification.company_sender = company_sender
    notification.company_receiver = company_receiver
    notification.save()
    
    send_email( notification=notification, receiver_profile=receiver_profile)
#-----------------------------------------------------

#sending notification in-app to the client after creating the invoice
def new_account(request, profile : Profile):

    send_notification(request,notification_type= NotificationType.NEW_ACCOUNT,
                service_title= f"{Welcome_message}.",
                company_sender_id= 8,
                company_receiver_id=profile.company_id
                )
    
#sending notification in-app to the client after creating the invoice
def account_modified(request,profile : Profile):

    send_notification(request,notification_type= NotificationType.ACCOUNT_MODIFIED,
                service_title= f"{account_modified_message}.",
                company_sender_id= 8,
                company_receiver_id=profile.company_id
                )

#sending notification in-app to the client after creating the invoice
def invoice_submitted(request, service : Service):

    send_notification(request,notification_type= NotificationType.INVOICE_SUBMITTED,
                service_title= f"{invoice_submitted_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_client.id
                )
    
#sending notification in-app to the client after updating the invoice
def invoice_updated(request, service : Service):

    send_notification(request,notification_type= NotificationType.INVOICE_MODIFIED,
                service_title= f"{invoice_updated_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_client.id
                )
    
#sending notification in-app to the client after updating the invoice
def invoice_deleted(request, service : Service):

    send_notification(request,notification_type= NotificationType.INVOICE_DELETED,
                service_title= f"{invoice_deleted_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_client.id
                )

#sending notification in-app to the client after creating the invoice
def invoice_request(request, service : Service):

    send_notification(request,notification_type= NotificationType.INVOICE_REQUEST,
                service_title= f"{invoice_request_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_provider.id
                )

#sending notification in-app to the client after creating the invoice
def invoice_verified(request, service : Service):

    send_notification(request,notification_type= NotificationType.INVOICE_VERIFIED,
                service_title= f"{invoice_verified_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_provider.id
                )
    
#sending notification in-app to the client after creating the invoice
def invoice_paid(request, service : Service):

    send_notification(request,notification_type= NotificationType.INVOICE_PAID,
                service_title= f"{invoice_paid_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_client.id
                )
    
#sending notification in-app to the client after creating the invoice
def invoice_rejected(request, service : Service):

    send_notification(request,notification_type= NotificationType.INVOICE_REJECTED,
                service_title= f"{invoice_rejected_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_provider.id
                )

#sending notification in-app to the client after updating the invoice
def service_updated(request, service : Service):

    send_notification(request,notification_type= NotificationType.SERVICE_MODIFIED,
                service_title= f"{service_updated_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_provider.id
                )

#sending notification in-app to the client after updating the invoice
def service_deleted(request, service : Service):

    send_notification(request,notification_type= NotificationType.SERVICE_DELETED,
                service_title= f"{service_deleted_message} {service.title}.",
                company_sender_id= request.profile.company_id,
                company_receiver_id=service.company_provider.id
                )
