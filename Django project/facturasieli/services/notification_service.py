# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/notification_service.py
# Author : Arnaud
# ---------------------------------------------------------------------------

from datetime import datetime

from django.shortcuts import get_object_or_404

from facturasieli.models import Company, Notification


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
