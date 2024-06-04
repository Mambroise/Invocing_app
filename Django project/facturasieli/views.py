# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views.py
# Author : Team
# ---------------------------------------------------------------------------

from facturasieli.views.index import index

from facturasieli.views.registration import register
from facturasieli.views.registration import create_otp
from facturasieli.views.registration import send_otp_mail
from facturasieli.views.registration import otp_validation
from facturasieli.views.registration import custom_log_in
from facturasieli.views.registration import log_out

from facturasieli.views.registration.transitions import welcome
from facturasieli.views.registration.transitions import goodbye

from facturasieli.views.profile import public_profile
from facturasieli.views.profile import edit_profile

from facturasieli.views.service import handle_service
from facturasieli.views.service import display_service
from facturasieli.views.service import delete_service

from facturasieli.views.verification import verify_invoice_view
<<<<<<< Updated upstream

from facturasieli.views.invoice import invoice_view
from facturasieli.views.invoice import invoice_success
=======
from facturasieli.views.verification import verify_invoice_list_view
>>>>>>> Stashed changes
