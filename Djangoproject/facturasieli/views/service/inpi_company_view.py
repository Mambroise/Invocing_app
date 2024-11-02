# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/select_company_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string

from facturasieli.forms import SearchForm
from facturasieli.services.inpi_company_search import INPICompanySearch
from facturasieli.services.create_company_service.create_company import create_company_from_api_data


def select_company(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    companies = None
    
    if 'inpi_client' not in request.session:
        messages.error(request, _('A problem occured, please sign in again'))
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    token = request.session['inpi_client']
    client = INPICompanySearch(token)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            siren = form.cleaned_data['search']
            try:
                data = client.search_by_siren(siren)
                company_data = data[0]
                print(company_data)
                companies=create_company_from_api_data(request,company_data)
            except Exception as e:
                print(e)
                companies = None
    else:
        form = SearchForm()
        # Remplace request.is_ajax() par la vérification de l'en-tête
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('facturasieli/service/company_results.html', {"companies": companies})
        return JsonResponse({"table": html})
    
    # Sinon, renvoie la page complète
    context = {"form": form, "companies": companies}

    return render(request, "facturasieli/service/select_company.html", context)