# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/send_email.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa

from facturasieli.models import Invoice

def generate_pdf_invoice(request,invoice_id,method):

    invoice = Invoice.objects.get(pk=invoice_id)

    # upload html template and invoice data
    html = render_to_string('facturasieli/pdf/invoice_pdf.html', {'invoice': invoice})

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = f'{method}; filename="invoice_{invoice.invoice_number}.pdf"'

    # Convert html into pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response