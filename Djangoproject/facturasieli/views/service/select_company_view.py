# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/select_company_view.py
# Author : Morice
# ---------------------------------------------------------------------------

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string

from facturasieli.forms.searchForm import SearchForm
from facturasieli.models import Company

def search_company_in_bdd(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    companies = []
    print("search_company_in_bdd")
    if request.method == 'POST':
        print("search_company_in_bdd dans le post")
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            try:
                companies = Company.objects.filter(name__icontains=search)
            except Company.DoesNotExist:
                companies = None

            if not companies:
                try:
                    companies = Company.objects.filter(siret__icontains=search)
                except Company.DoesNotExist:
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
