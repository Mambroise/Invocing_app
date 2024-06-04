# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/notification/show_notification.py
# Author : Arnaud
# ---------------------------------------------------------------------------

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from facturasieli.models import Notification, Profile


def show_notification(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_flog_in'))
    
    user_email = request.user.email
    profil_user = get_object_or_404(Profile, email= user_email )
    list_notifications_received = Notification.objects.all().filter(company_receiver=profil_user.company)
    
    list_notifications_sended = Notification.objects.all().filter(company_sender=profil_user.company)
   
    context={
        'notifications_received': list_notifications_received,
        'notifications_sended' : list_notifications_sended
    }
    return render(request, 'notification/show_notification.html', context)
