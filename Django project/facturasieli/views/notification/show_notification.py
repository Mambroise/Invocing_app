# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/notification/show_notification.py
# Author : Arnaud,Morice
# ---------------------------------------------------------------------------
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Notification, Profile


def show_notification(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    context = get_user_notification_pagination(request)
    return render(request, 'notification/show_notification.html', context)


# changes the notification status to true (is_read)and timestamp opening time when the user opens it
def handle_open_notification(request: HttpRequest, notification_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    # Récupérer la notification dont la pk = notification_id
    notification = get_object_or_404(Notification, pk=notification_id)
    
    # Marquer la notification comme lue
    notification.is_read = True

    # Enregistrer l'heure de lecture
    notification.is_read_timestamp = timezone.now() 
    notification.save()

    context = get_user_notification_pagination(request)
    return render(request, 'notification/show_notification.html', context)

def delete_notification(request, notification_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    notification_to_delete = Notification.objects.filter(pk=notification_id)
    notification_to_delete.delete()

    context = get_user_notification_pagination(request)
    return render(request, 'notification/show_notification.html', context)

def get_user_notification_pagination(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    user_email = request.profile.email
    profil_user = get_object_or_404(Profile, email= user_email )

    # paginate received notifications by batches of 15
    notifications_received_list = Notification.objects.filter(company_receiver=profil_user.company)
    paginator_received_notifs = Paginator(notifications_received_list,15)

    # get the request attribute page number and select corresponding page
    received_page_number = request.GET.get('page_received')

    try:
        notifications_received = paginator_received_notifs.page(received_page_number)
    except PageNotAnInteger:
        notifications_received = paginator_received_notifs.page(1)
    except EmptyPage:
        notifications_received = paginator_received_notifs.page(paginator_received_notifs.num_pages)

    # paginate sent notifications by batches of 15
    notifications_sent_list = Notification.objects.filter(company_sender=profil_user.company)
    paginator_sent_notifs = Paginator(notifications_sent_list,15)

    # get the request attribute page number and select corresponding page
    sent_page_number =  request.GET.get('page_sent')

    try:
        notifications_sended = paginator_sent_notifs.page(sent_page_number)
    except PageNotAnInteger:
        notifications_sended = paginator_sent_notifs.page(1)
    except EmptyPage:
        notifications_sended = paginator_sent_notifs.page(paginator_sent_notifs.num_pages)

   
    context={
        'notifications_received': notifications_received,
        'notifications_sended' : notifications_sended
    }

    return context