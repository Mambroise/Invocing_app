# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/all_maths.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.shortcuts import get_object_or_404
from facturasieli.models import Service

@staticmethod
def invoice_total_amount(invoice):

    # Total price math
    try:
        if invoice.tax == 1:
            vat = 20
        elif invoice.tax == 2:
            vat = 10
        elif invoice.tax == 4:
            vat = 5.5
        elif invoice.tax == 5:
            vat = 2.1
        total_price = invoice.amount_excluding_tax + (invoice.amount_excluding_tax * (vat / 100))
    except:
        total_price = 0

    return total_price