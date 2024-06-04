# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/__init__.py
# Author : Team
# ---------------------------------------------------------------------------

from .transitions import *

from .create_otp_view import create_otp
from .custom_log_in_view import custom_log_in
from .log_out_view import log_out
from .otp_validation_view import otp_validation
from .register_view import register
from .send_otp_mail_view import send_otp_mail
