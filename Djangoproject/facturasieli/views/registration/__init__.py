# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/__init__.py
# Author : Team
# ---------------------------------------------------------------------------

from .transitions import *

from .custom_log_in_view import custom_log_in
from .log_out_view import log_out
from .otp_validation_view import otp_validation
from .register_view import register
from .company_address_view import register_company_address
from .inpi_company_view import select_company
from .company_address_form_view import company_address_form
