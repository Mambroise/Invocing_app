# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/urls.py
# Author : Team
# ---------------------------------------------------------------------------

from django.contrib.auth import views as auth_views
from django.urls import path

from facturasieli import views


app_name = 'facturasieli'
urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register, name='register'),
    path('register2/', views.register_company_address, name='register2'),
    path('welcome/', views.welcome, name='welcome'),

    path('custom_login/', views.custom_log_in, name='custom_log_in'),
    path('otp_validation/', views.otp_validation, name='otp_validation'),

    path('logout/', views.log_out, name='log_out'),
    path('goodbye/', views.goodbye, name='goodbye'),

    path('public_profile/<int:user_id>/', views.public_profile, name='public_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('service_form/', views.handle_service, name='service_form'),
    path('service/<int:company_id>/', views.display_service, name='service'),
    path('show_service/<int:service_id>/', views.show_service, name='show_service'),
    path('delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
    path('update_service/<int:service_id>/', views.update_service, name='update_service'),

    path('invoice/<int:service_id>/', views.invoice_view, name='invoice_form'),
    path('delete_invoice/<int:service_id>/', views.delete_invoice, name='delete_invoice'),
    path('update_invoice/<int:service_id>/', views.update_invoice, name='update_invoice'),
    
    path('notification/', views.show_notification, name='show_notification'),
    path('notification/<int:notification_id>', views.handle_open_notification, name='change_notif_status'),

    path('invoices/<int:invoice_id>/', views.verify_invoice_view, name='verify_invoice'),
    path('invoices/verification/', views.verify_invoice_list_view, name='verification_list'),
]
