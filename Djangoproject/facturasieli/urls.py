# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/urls.py
# Author : Team
# ---------------------------------------------------------------------------

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from facturasieli import views


app_name = 'facturasieli'
urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register, name='register'),
    path('register2/', views.register_company_address, name='register2'),

    path('custom_login/', views.custom_log_in, name='custom_log_in'),
    path('otp_validation/', views.otp_validation, name='otp_validation'),

    path('logout/', views.log_out, name='log_out'),
    path('goodbye/', views.goodbye, name='goodbye'),

    path('public_profile/<int:user_id>/', views.public_profile, name='public_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_company/', views.edit_company, name='edit_company'),
    path('account_check/', views.account_check, name='account_check'),
    path('reset_password/<int:profile_id>/', views.reset_password, name='reset_password'),

    path('select_company/', views.search_company, name='select_company'),
    path('service_form/<int:company_id>', views.handle_service, name='service_form'),
    path('service/', views.display_service, name='service'),
    path('show_service/<int:service_id>/', views.show_service, name='show_service'),
    path('delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
    path('update_service/<int:service_id>/', views.update_service, name='update_service'),

    path('invoice/<int:service_id>/', views.invoice_view, name='invoice_form'),
    path('delete_invoice/<int:service_id>/', views.delete_invoice, name='delete_invoice'),
    path('update_invoice/<int:service_id>/', views.update_invoice, name='update_invoice'),
    path('print_invoice/<int:invoice_id>/', views.print_invoice, name='print_invoice'),
    path('download_bis/<int:invoice_id>/', views.download_bis, name='download_bis'),
    
    path('notification/', views.show_notification, name='show_notification'),
    path('notification/<int:notification_id>', views.handle_open_notification, name='change_notif_status'),
    path('delete_notification/<int:notification_id>', views.delete_notification, name='delete_notification'),

    path('invoices_verif/<int:invoice_id>/', views.verify_invoice_view, name='verify_invoice'),
    path('update_verification/<int:invoice_id>/', views.update_verification, name='update_verification'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
