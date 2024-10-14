# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/select_company_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import HttpResponseRedirect
from django.urls import reverse

from facturasieli.services.inpi_company_search import INPICompanySearch

def select_company(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    if 'inpi_client' in request.session:
        token = request.session['inpi_client']
        client = INPICompanySearch(token)
        print(client)

    