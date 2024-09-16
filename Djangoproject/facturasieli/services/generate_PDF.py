# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/services/send_email.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa

from facturasieli.models import Invoice,Company
from facturasieli.services.all_maths import invoice_total_amount

def generate_pdf_invoice(request,invoice_id,method):

    # data treatment
    invoice = Invoice.objects.get(pk=invoice_id)
    provider_name = invoice.name_provider
    client_name = invoice.name_client
    provider = Company.objects.get(name=provider_name)
    client = Company.objects.get(name=client_name)
    total_price = invoice_total_amount(invoice)

    # upload html template and invoice data
    invoice_data = {'invoice': invoice, 'total_price':total_price, 'provider':provider, 'client':client }
    html = render_to_string('facturasieli/pdf/invoice_pdf.html', invoice_data)

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'{method}; filename="invoice_{invoice.invoice_number}.pdf"'

    # Convert html into pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response